#!/usr/bin/env python3
"""Calculate football lottery odds probabilities and value metrics."""

import argparse
import json
from math import isfinite


def positive_float(value):
    parsed = float(value)
    if not isfinite(parsed) or parsed <= 0:
        raise argparse.ArgumentTypeError("value must be a positive finite number")
    return parsed


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute implied probabilities, no-vig probabilities, fair odds, EV, and Kelly fractions from decimal odds."
    )
    parser.add_argument("--odds", nargs="+", type=positive_float, required=True, help="Decimal odds for mutually exclusive outcomes.")
    parser.add_argument("--labels", nargs="+", help="Outcome labels. Defaults to outcome_1, outcome_2, ...")
    parser.add_argument("--model", nargs="+", type=positive_float, help="Model probabilities as decimals or percentages.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Output format.")
    return parser.parse_args()


def normalize_probabilities(values):
    probs = [value / 100.0 if value > 1 else value for value in values]
    total = sum(probs)
    if total <= 0:
        raise ValueError("model probabilities must sum to a positive value")
    return [value / total for value in probs]


def kelly_fraction(decimal_odds, probability):
    b = decimal_odds - 1.0
    if b <= 0:
        return 0.0
    q = 1.0 - probability
    return max(((b * probability) - q) / b, 0.0)


def build_rows(labels, odds, model):
    implied = [1.0 / odd for odd in odds]
    overround = sum(implied)
    no_vig = [prob / overround for prob in implied]
    model_probs = normalize_probabilities(model) if model else None

    rows = []
    for index, label in enumerate(labels):
        row = {
            "label": label,
            "odds": odds[index],
            "implied_probability": implied[index],
            "no_vig_probability": no_vig[index],
        }
        if model_probs:
            p = model_probs[index]
            roi = odds[index] * p - 1.0
            kelly = kelly_fraction(odds[index], p)
            row.update(
                {
                    "model_probability": p,
                    "fair_odds": (1.0 / p) if p > 0 else None,
                    "expected_roi": roi,
                    "kelly_fraction": kelly,
                    "quarter_kelly_fraction": kelly * 0.25,
                }
            )
        rows.append(row)

    return {
        "overround": overround,
        "market_margin": overround - 1.0,
        "rows": rows,
    }


def pct(value):
    return f"{value * 100:.2f}%"


def decimal(value):
    return "" if value is None else f"{value:.3f}"


def print_markdown(result):
    has_model = "model_probability" in result["rows"][0]
    headers = ["Outcome", "Odds", "Implied", "No-vig"]
    if has_model:
        headers.extend(["Model", "Fair odds", "Exp. ROI", "Kelly", "1/4 Kelly"])
    print(f"Market margin: {pct(result['market_margin'])}")
    print()
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["---"] + ["---:"] * (len(headers) - 1)) + " |")
    for row in result["rows"]:
        values = [
            row["label"],
            f"{row['odds']:.3f}",
            pct(row["implied_probability"]),
            pct(row["no_vig_probability"]),
        ]
        if has_model:
            values.extend(
                [
                    pct(row["model_probability"]),
                    decimal(row["fair_odds"]),
                    pct(row["expected_roi"]),
                    pct(row["kelly_fraction"]),
                    pct(row["quarter_kelly_fraction"]),
                ]
            )
        print("| " + " | ".join(values) + " |")


def main():
    args = parse_args()
    if any(odd <= 1.0 for odd in args.odds):
        raise SystemExit("decimal odds must be greater than 1.0")

    labels = args.labels or [f"outcome_{index + 1}" for index in range(len(args.odds))]
    if len(labels) != len(args.odds):
        raise SystemExit("--labels must have the same length as --odds")
    if args.model and len(args.model) != len(args.odds):
        raise SystemExit("--model must have the same length as --odds")

    result = build_rows(labels, args.odds, args.model)
    if args.format == "markdown":
        print_markdown(result)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
