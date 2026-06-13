---
name: football-lottery-advisor
description: Data-driven Chinese football lottery recommendation workflow for source-backed pre-match analysis using China Sports Lottery / 中国体育彩票玩法. Use when Codex needs to analyze 足彩, 足球彩票, 竞彩足球, 传统足彩, 胜平负, 让球胜平负, 比分, 总进球数, 半全场胜平负, 混合过关, 14场胜负, 任九, 6场半全场, 4场进球, probability edges, or no-bet decisions for soccer matches. Always verify current fixtures, Chinese lottery odds, team news, and rules before giving picks.
---

# Football Lottery Advisor

## Overview

Use this skill to produce source-backed Chinese football lottery recommendations with explicit probability, value, and risk reasoning. Treat every pick as uncertain decision support, not a promise of profit.

## Operating Rules

- Verify current data for a named match/date before recommending: fixture, kickoff time, venue, latest injuries/suspensions, expected lineups, recent form, schedule load, odds/line movement, and weather when relevant.
- Cite sources and state the data timestamp. If current sources are unavailable or conflict materially, output `暂不推荐` with missing-data reasons.
- Never present a pick as `必中`, `稳赚`, `包红`, or guaranteed. Do not encourage chasing losses, borrowing, or increasing stake after losses.
- Use unit sizing only when the user asks for staking guidance; keep it conservative and framed as risk management, not financial advice.
- Prefer single-match recommendations. Avoid long parlays unless the user explicitly asks for `串关`; flag parlays as higher variance.
- In Chinese outputs, use the Chinese names commonly used by Chinese football fans for players, coaches, and well-known team nicknames. Do not leave player names in English in the final answer; when unsure, verify Chinese sources or use a reasonable Chinese transliteration instead of raw English.
- Use China Sports Lottery / 中国体育彩票玩法 as the betting vocabulary and recommendation boundary. Do not recommend unsupported markets such as Asian handicap, over/under goals, corners, cards, player props, or exchange-style bets unless explicitly translating them into a supported Chinese lottery market.
- Treat official Chinese lottery settlement as full-time 90 minutes including stoppage time, excluding extra time and penalties, unless the official rules for a named game state otherwise.
- Unless the user explicitly asks for `不要表情`, `无表情`, or `纯文本`, include emoji markers on all major section headings. Do not output plain headings such as `预测结论`, `比赛定性`, or `反方风险` without their emoji prefixes.
- Default `小红书版` output must use the fixed Qianwen-style 6-section emoji template in `references/recommendation-framework.md`: `预测结论`, `比赛定性`, `预测理由`, `进球预测`, `场外因素`, `总结`. The `预测结论` section must keep the compact decision table and include at least 3 recommendation rows ordered from conservative to balanced to aggressive, with risk and potential odds return increasing by row. `预测理由` and `场外因素` must both use numbered emoji subpoints, not a single paragraph. Each major section body must contain at least 100 Chinese characters unless the user explicitly asks for a shorter answer; if data is missing, fill the section with the missing-data note and its impact on confidence instead of deleting or merging the section.

## Workflow

1. Define scope: identify competition, date, match list, Chinese lottery category (`竞彩足球` or `传统足彩`), official market type (`胜平负`, `让球胜平负`, `比分`, `总进球数`, `半全场胜平负`, `混合过关`, `14场胜负`, `任选9`, `6场半全场`, `4场进球`), and whether the user wants picks, risk review, or a full note.
2. Build evidence pack: collect current fixture data, team news, likely lineups, tactical matchup, standings/motivation, recent performance, home/away splits, rest/travel, and market odds.
3. Normalize Chinese lottery odds: convert fixed bonus/decimal-style odds to implied probabilities, remove overround for mutually exclusive outcomes, compare with the model estimate, and identify value only when the estimated edge is positive and the evidence quality is adequate.
4. Score the match: weigh baseline team strength, form, team news, tactical matchup, motivation/schedule, market signal, and environment. Read `references/china-lottery-playtypes.md` before analyzing unfamiliar Chinese lottery markets, and read `references/recommendation-framework.md` for the detailed rubric when preparing notes.
5. Decide recommendation class: classify each option as `主推`, `次选`, `谨慎`, or `暂不推荐`; include the strongest counterargument for every recommended pick.
6. Produce the answer: choose `小红书版` by default, or use `专业分析师版` / `公众号版` when the user asks for that tone. Use a strong-opinion but risk-bounded structure: conclusion first, then match framing, pre-match information table, team-by-team analysis, reasons, Chinese lottery odds/probability, score or total-goals reference, match scripts, off-field factors, counterargument, and final recommendation card. Always preserve source timestamp, Chinese lottery terms, counterargument, risk wording, and Chinese-translated player names.

## Recommended Output

Use a strong-opinion Chinese recommendation style that fits the user's requested channel:

1. `小红书版`: default style; use the fixed Qianwen-style 6-section emoji template, keep the compact decision table in `预测结论`, and use richer emojis plus punchier takeaways. Each major section body must be at least 100 Chinese characters unless the user explicitly asks for a shorter answer.
2. `专业分析师版`: most complete formal style; open with a firm stance, then bind every claim to evidence, Chinese lottery odds, probability, and risk. Unless the user asks for brevity, single-match outputs should be full-length and not a short card. Use visible emoji anchors on every major section.
3. `公众号版`: use a stronger article title, match framing, multi-section reasoning, match script analysis, a final Chinese lottery recommendation card, and emoji-marked headings throughout.

Read `references/china-lottery-playtypes.md` when mapping a user's request to official Chinese football lottery markets. Read `references/recommendation-framework.md` for the full templates before writing public-account, Xiaohongshu, or analyst-style notes. Do not imitate hype accounts: avoid `必中`, `包红`, `回血`, `重仓`, `上车`, or urgency language.

## Tools

- Use `scripts/value_calc.py` to compute implied probabilities, no-vig probabilities, fair odds, expected ROI, and Kelly fractions from decimal odds and model probabilities.
- Use `references/china-lottery-playtypes.md` for official Chinese football lottery market mapping and settlement assumptions.
- Use `references/recommendation-framework.md` for scoring, confidence tiers, market guidance, and Chinese style templates.

Example:

```bash
python3 /Users/fanzhengjia/.codex/skills/football-lottery-advisor/scripts/value_calc.py \
  --labels 胜 平 负 \
  --odds 1.90 3.45 4.20 \
  --model 0.56 0.25 0.19 \
  --format markdown
```
