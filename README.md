# football-lottery-advisor

A Codex skill for source-backed Chinese football lottery analysis.

This skill helps produce pre-match recommendations for China Sports Lottery football markets such as `竞彩足球`, `胜平负`, `让球胜平负`, `比分`, `总进球数`, `半全场胜平负`, `混合过关`, `14场胜负`, and `任选9`.

It is designed for decision support only. It does not guarantee outcomes, profit, or betting success.

## What It Does

- Verifies current fixture, team news, odds, lineup, venue, and market context before giving a pick.
- Maps recommendations to official China Sports Lottery market names and settlement assumptions.
- Computes implied probabilities, no-vig probabilities, fair odds, expected ROI, and Kelly fractions from decimal odds.
- Produces Chinese recommendation notes with probability, value, counterargument, and risk language.
- Avoids unsupported betting markets unless translated into supported Chinese lottery play types.

## Structure

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── china-lottery-playtypes.md
│   └── recommendation-framework.md
└── scripts/
    └── value_calc.py
```

## Usage

Install or copy this folder into your Codex skills directory, then invoke:

```text
$football-lottery-advisor 分析 德国 vs 库拉索
```

Run the value calculator directly:

```bash
python3 scripts/value_calc.py \
  --labels 胜 平 负 \
  --odds 1.90 3.45 4.20 \
  --model 0.56 0.25 0.19 \
  --format markdown
```

## Safety Notes

- This project is analytical tooling, not financial advice.
- All recommendations should be treated as uncertain pre-match probability judgments.
- Current fixture, odds, injuries, lineups, and rules must be verified before use.
- Do not use this skill to promote guaranteed wins, chasing losses, borrowing to bet, or high-risk staking.

## License

MIT
