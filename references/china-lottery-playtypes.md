# Chinese Football Lottery Play Types

Use this reference to map any football recommendation request to China Sports Lottery / 中国体育彩票玩法. If a user asks for a market outside these categories, either translate it into the closest official Chinese lottery market or say that the requested market is outside the skill's足彩 scope.

## Core Settlement Rule

Default to full-time 90 minutes including stoppage time, excluding extra time and penalty shootouts. Re-check official rules if a special tournament or named game states otherwise.

## 竞彩足球

Use official Chinese lottery market names in final recommendations.

| Market | Chinese output | Outcome set | Notes |
| --- | --- | --- | --- |
| 胜平负 | `胜/平/负` or `3/1/0` | Home win, draw, away win | Always from the listed home team's perspective. |
| 让球胜平负 | `让胜/让平/让负` | Home team result after official let-ball adjustment | The let-ball number belongs to the home team. `-1` means home gives one goal; `+1` means home receives one goal. |
| 比分 | exact score plus `胜其他/平其他/负其他` | Official 31-option score set | Home score appears first. High variance. |
| 总进球数 | `0/1/2/3/4/5/6/7+` | Total goals by both teams | Do not write generic `大/小球` as the final pick. |
| 半全场胜平负 | `胜胜/胜平/胜负/平胜/平平/平负/负胜/负平/负负` | Half-time home result + full-time home result | High variance. |
| 混合过关 | official market combinations | Selected legs must all be correct | Use only official Chinese lottery markets in the combination. |

Output examples:

- `竞彩胜平负：胜`
- `竞彩让球胜平负：主队 -1，让负`
- `竞彩总进球数：2球`
- `竞彩比分：1:1 / 2:1`
- `竞彩半全场：平胜`

## 传统足彩

Use when the user asks for traditional pools, full round selections, or `14场/任九/6场半全场/4场进球`.

| Market | Chinese output | Selection style |
| --- | --- | --- |
| 14场胜负 | per-match `3/1/0` or `胜/平/负` | Provide single, double, or triple selections when needed. |
| 任选9 | choose 9 matches from the 14-match pool | Explain why each excluded match is risky. |
| 6场半全场 | half-time/full-time result | Use official half/full combinations. |
| 4场进球 | each team's goals | Use `0/1/2/3+` for each listed team. |

## Mapping Rules

- If the source uses decimal odds, treat them as fixed bonus style odds for probability math, but label the final recommendation using Chinese lottery terms.
- If the source uses Asian handicap or over/under, do not output that market directly. Map only when a corresponding Chinese lottery market is available:
  - Asian side lean -> `胜平负` or `让球胜平负`
  - Total goals lean -> `总进球数`
  - Exact score lean -> `比分`
- For `让球胜平负`, always show the official let-ball number and explain the adjusted-result condition in plain Chinese.
- For parlays, use `串关` or `混合过关`; avoid international betting notation unless it is only used as background.
