# Football Lottery Recommendation Framework

Use this reference when preparing a full Chinese football lottery note, comparing several matches, or assigning confidence tiers. For official market mapping and settlement assumptions, read `china-lottery-playtypes.md`.

## Evidence Checklist

- Fixture: competition, kickoff time, home/away, venue, travel distance, time zone.
- Team state: injuries, suspensions, expected lineup, rotation risk, coach comments, recent minutes, rest days.
- Performance: recent xG if available, shots, chance quality, home/away split, table position, strength of opponents.
- Tactical matchup: pressing resistance, transition defense, set pieces, wide/central overloads, striker availability, goalkeeper quality.
- Motivation and schedule: title/relegation/cup priority, derby pressure, second leg context, congested fixtures.
- Market: current Chinese lottery odds, official let-ball number, selected play type, odds movement when available, consensus versus outlier prices.
- Environment: weather, pitch, altitude, travel fatigue, crowd restrictions.

## Scoring Rubric

Use the score to discipline reasoning; do not present it as a precise prediction.

| Factor | Weight | What to Check |
| --- | ---: | --- |
| Baseline strength | 20 | Ratings, table quality, squad value, long-run performance |
| Recent performance | 15 | Last 5-10 matches, xG trend, opponent strength |
| Team news | 20 | Injuries, suspensions, lineup certainty, rotation |
| Tactical matchup | 10 | Style conflicts, set-piece edge, transition risk |
| Motivation/schedule | 10 | Rest, travel, competition priority, game state incentives |
| Market signal | 20 | Odds movement, no-vig probability, price dispersion |
| Environment | 5 | Weather, venue, pitch, crowd, travel |

Confidence tiers:

- `A`: current data is strong, model probability clearly beats market, key risks are understood.
- `B`: evidence supports the pick, but edge or data quality is moderate.
- `C`: lean only; acceptable for discussion, usually not a main pick.
- `暂不推荐`: no positive value, conflicting signals, stale data, high lineup uncertainty, or price already moved.

## Market Math

- Decimal implied probability: `1 / odds`.
- Market overround: sum of implied probabilities across all mutually exclusive outcomes.
- No-vig probability: each implied probability divided by overround.
- Fair odds from model probability: `1 / model_probability`.
- Expected ROI per unit: `decimal_odds * model_probability - 1`.
- Kelly fraction for decimal odds: `((odds - 1) * p - (1 - p)) / (odds - 1)`.

Only treat an option as value when the edge is positive after conservative probability estimates. If model probability is mostly judgmental, downshift confidence by at least one tier.

## Market Guidance

- `胜平负`: best for clear side/value opinions; draw risk must be discussed.
- `让球胜平负`: use the official Chinese lottery let-ball number shown for the home team. `-1` means the home team gives one goal; `+1` means the home team receives one goal. Recommend `让胜/让平/让负`, not generic Asian handicap wording.
- `总进球数`: recommend one of `0/1/2/3/4/5/6/7+`, not over/under wording. Use pace, xG, defensive absences, finishing variance, weather, and game incentives.
- `比分`: use the official score buckets including exact scores and `胜其他/平其他/负其他`. High variance; recommend only when the user asks or as a secondary reference.
- `半全场胜平负`: use official combinations such as `胜胜/胜平/胜负/平胜/平平/平负/负胜/负平/负负`. High variance; avoid making it the main pick without a clear reason.
- `混合过关`: combine official Chinese lottery markets only. Explain correlation and variance.
- `传统足彩`: for `14场胜负` and `任选9`, output `3/1/0` or `胜/平/负` selections per match; for `6场半全场`, output half/full combinations; for `4场进球`, output each team's 0/1/2/3+ goal count.

## Style Templates

Use the requested style without diluting the analysis. If the user does not specify a style, use `小红书版`. The preferred output is now a strong-opinion systematic note: it should read with the clarity and rhythm of a social sports preview, but keep probability, Chinese lottery rules, and risk discipline.

Shared requirements:

- Start with the conclusion, not background.
- Include data timestamp and sources after the recommendation or at the end.
- Include at least one counterargument for every recommended pick.
- State whether the pick is `主推`, `次选`, `谨慎`, or `暂不推荐`.
- Default to detailed output. Do not collapse a single-match recommendation into a few short paragraphs unless the user explicitly asks for `简短`, `只要结论`, or `精简`.
- For a single match, include at least 10 distinct evidence points across team state, recent form, injury/lineup, tactical matchup, Chinese lottery odds, motivation/schedule, environment, and risk. If data is unavailable, state the gap and how it affects confidence.
- Default `小红书版` is a fixed Qianwen-style 6-section format: `预测结论`, `比赛定性`, `预测理由`, `进球预测`, `场外因素`, `总结`. Do not remove, rename, merge, or reorder its sections unless the user explicitly requests another style or a shorter answer. The `预测结论` section must keep the compact decision table and must include at least 3 recommendation rows ordered by a separate `风险档位` column as `稳健档`, `平衡档`, and `博高赔`; risk and potential odds return must increase by row. The `推荐` column must contain only the China-lottery pick direction, not the risk tier. Each major section body must contain at least 100 Chinese characters; the heading and table header do not count.
- Use `A/B/C + 星级` for confidence, such as `B｜★★★★☆`. Stars express subjective confidence only and are not a hit-rate promise.
- Use Chinese fan-standard translations for player, coach, and common team nickname references. Prefer Chinese sports media conventions such as `维尼修斯`, `拉菲尼亚`, `麦克托米奈`, `阿什拉夫`, `齐耶赫`, `恩内斯里`, `内马尔`, `罗伯逊`, `麦金`, `尚克兰`. Do not output raw English player names in Chinese-style notes.
- If a name is obscure and no common Chinese translation is immediately reliable, create a clear Chinese transliteration and keep the original English name out of the public-facing text.
- Avoid promotional or certainty language such as `必中`, `包红`, `回血`, `重仓`, `稳胆`, `上车`, `闭眼买`, `错过可惜`, `稳稳收米`, or `赌一把`.
- Use emojis as required visual anchors, not as proof. Unless the user explicitly asks for `不要表情`, `无表情`, or `纯文本`, every major section heading must start with an emoji.
- Minimum emoji anchors by style: at least 8 in `专业分析师版`, at least 10 in `公众号版`, and exactly the fixed 6 major emoji headings in default `小红书版`, with numbered emoji subpoints under both `预测理由` and `场外因素`. Do not strip emoji headings even for serious analysis.
- Recommended emoji vocabulary: `🎯` conclusion, `📌` pick, `📊` odds/probability, `🧠` analysis, `⚔️` tactical matchup, `🚑` injuries, `🌦️` weather, `⚠️` risk, `✅` final card, `📝` source note.
- Never use emojis to imply certainty or urgency. Avoid celebratory betting emojis around risky picks.
- Before finalizing, scan the draft: if a major heading appears as plain text (`预测结论`, `比赛定性`, `赛前信息`, `竞彩赔率与概率`, `预测理由`, `比赛脚本`, `场外因素`, `反方风险`, `最终推荐卡`), rewrite it with the matching emoji prefix.

## Unified Strong-Opinion Skeleton

Use this skeleton as the content backbone for strong-opinion outputs. The default `小红书版` must keep these 6 top-level emoji sections exactly; other styles may expand them, but should not remove the conclusion table, Chinese lottery market, probability/odds, counterargument, or final card.

```text
🎯 预测结论
| 风险档位 | 比赛 | 竞彩玩法 | 推荐 | 信心 | 估计概率 | 公允赔率 | 当前赔率 | 核心理由 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| 稳健档 | [主队] vs [客队] | [低风险中国足彩玩法] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |
| 平衡档 | [主队] vs [客队] | [中风险中国足彩玩法] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |
| 博高赔 | [主队] vs [客队] | [高风险中国足彩玩法] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |

[表格后写强观点结论：说明三档推荐为什么按稳健档、平衡档、博高赔排序，风险和潜在赔率回报如何递增；再写主推/次选/谨慎/暂不推荐、比分参考、总进球数参考、为什么不是简单追热门或搏冷。不要把潜在回报写成收益承诺。]

⚖️ 比赛定性
[用千问式强定性写法定义比赛：强弱分明、热门过热、让球陷阱、拉锯防冷、进球数低开高走等。必须交代赛事背景、时间地点、市场关注点、双方定位和最容易被误判的点。]

🧠 预测理由
1. 🔥 状态火力：[近期战绩、进攻效率、防守稳定性、对手质量、核心球员中文译名。]
2. 🚑 伤停阵容：[确认缺席、出战成疑、停赛、轮换风险，以及这些变化影响的区域。]
3. ⚔️ 战术对位：[边路/中路攻防、压迫与反压迫、定位球、转换进攻、身后空间。]
4. 📈 阵容厚度/实力差：[排名、身价、联赛质量、替补深度、关键位置层级差。]
5. 🗓️ 战意赛程：[小组/积分形势、杯赛优先级、休息天数、旅途消耗、临场战意。]
6. 📊 竞彩赔率与概率：[中国足彩玩法、当前赔率、市场去水概率、我的估计概率、公允赔率、价值判断和临场赔率阈值。]

⚽ 进球预测
[把进球判断映射到中国足彩的 `总进球数` 和 `比分`，比分只做参考，不替代主推荐。说明先进球路径、可能的节奏变化、最可能的比分区间和冷门比分触发条件。]

🌦️ 场外因素
1. 🌧️ 天气场地：[必须单独成点。写天气、温度、风雨、草皮、场地尺寸或中立场；未确认则写不纳入主判断，并说明可能影响进球数、对抗强度还是传控质量。]
2. 🧳 旅途时差：[必须单独成点。写跨洲飞行、休息天数、连续客场、赛程密度和适应问题；没有证据则说明缺口，不能脑补。]
3. 👨‍⚖️ 裁判尺度：[必须单独成点。若有可靠来源，写犯规、点球、红黄牌倾向及其对节奏的影响；无来源则明确不纳入主判断。]
4. 🏟️ 主客与氛围：[必须单独成点。写主场、中立场、观众结构、草皮熟悉度和心理压力，并说明对压迫、防守稳定性或反击效率的影响。]
5. 📝 信息缺口：[必须单独成点。列出首发、赔率、天气、伤停中未确认的内容，并说明哪些变化会让推荐降级或转向暂不推荐。]

✅ 总结
[用最终推荐卡收束：比赛、主推、次选、比分参考、总进球数参考、定位、信息时间、临场复核点。必须写最可能打穿推荐的反向路径，并补一句：这是赛前概率判断，不是收益承诺。]
```

### 专业分析师版

Best for serious decision support, multi-match comparisons, and users who ask for probability or value analysis. Use the full skeleton and keep the language forceful but measured.

Depth requirements for one match:

- Target roughly 1,200-1,800 Chinese characters when enough current data is available.
- Include the compact decision table plus at least 8 sections: `预测结论`, `比赛定性`, `赛前信息表`, `竞彩赔率与概率`, `预测理由`, `进球与比分预测`, `比赛脚本推演`, `场外因素`, `反方观点`, `最终推荐卡`.
- Each `预测理由` module should contain 2-3 sentences, not a one-line label.
- Add `信息缺口` when lineup, Chinese lottery odds, weather, or injuries cannot be confirmed.

Start with a compact decision table:

| 风险档位 | 比赛 | 竞彩玩法 | 推荐 | 信心 | 估计概率 | 公允赔率 | 当前赔率 | 核心理由 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |

Follow with this structure:

```text
🎯 预测结论
本场倾向：[竞彩玩法 + 方向]
信心：[A/B/C｜星级]
定位：[主推/次选/谨慎/暂不推荐]
比分参考：[x-x / x-x]；总进球数参考：[x球]

⚖️ 比赛定性
[2-4 句定义本场：热门是否过热、让球是否有坑、弱队是否有守住空间、比赛会如何进入主推荐脚本]

📋 赛前信息表
| 项目 | 信息 |
| --- | --- |
| 赛事/时间 | [赛事 + 北京时间] |
| 场地/天气 | [场地 + 天气；未确认则写未确认] |
| 中国足彩玩法 | [竞彩足球/传统足彩 + 具体玩法] |
| 关键伤停 | [中文译名 + 状态] |
| 信息时间 | [YYYY-MM-DD HH:mm 时区] |

📊 竞彩赔率与概率
- 概率：模型估计 [x%]，市场去水约 [x%]
- 赔率：当前 [x.xx]，公允 [x.xx]，价值差 [x%]
- 信息时间：[YYYY-MM-DD HH:mm 时区]

🧠 预测理由
1. 🔥 主队状态与火力：[2-3 句]
2. 🧊 客队状态与抗压：[2-3 句]
3. 🚑 伤停与阵容：[2-3 句]
4. ⚔️ 战术对位：[2-3 句]
5. 🧱 阵容厚度/实力差：[2-3 句]
6. 🗓️ 战意与赛程：[2-3 句]

⚽ 进球与比分预测
[2-4 句，映射到竞彩总进球数和比分，不写非中国足彩市场]

🧩 比赛脚本推演
- 正向脚本：[推荐最容易命中的比赛路径]
- 中性脚本：[推荐仍可能命中的胶着路径]
- 反向脚本：[推荐失效的比赛路径]

🌦️ 场外因素
[天气、场地、裁判、旅途分项写；已确认因素写入，未确认则标注不纳入主判断]

📝 信息缺口
- [列出未确认数据及其可能改变的结论；没有缺口则写“当前主要信息已覆盖，仍需临场复核首发和赔率”]

⚠️ 反方观点：
- [最可能推翻推荐的因素]

✅ 最终推荐卡
- 主推：[竞彩玩法 + 方向]
- 次选：[可选]
- 比分参考：[可选]
- 总进球数参考：[可选]
- 串关/混合过关：仅在用户要求时给出，并说明相关性和方差
```

### 公众号版

Best for longer Chinese article output. Use a stronger title, clear match framing, multi-section reasons, and a final card. Keep the rhythm similar to a sports preview article, but do not use exaggerated betting-account language.

Depth requirements for one match:

- Target roughly 1,800-2,600 Chinese characters when enough current data is available.
- Each of `比赛定性`, `预测理由`, `竞彩赔率与概率`, `进球与比分预测`, `最大风险` should contain enough explanation to stand alone as a short article section.
- Use punchy lead sentences, but follow each lead with evidence or probability reasoning.

```text
# 🎯 [标题：比赛 + 核心判断]

## 🎯 预测结论
先说结论：本场我更倾向 [竞彩玩法 + 方向]，信心 [A/B/C｜星级]，定位 [主推/次选/谨慎/暂不推荐]。
比分参考：[x-x / x-x]；总进球数参考：[x球]。

## ⚖️ 一、比赛定性
[3-5 句交代赛事背景、双方状态、市场关注点，用强观点给本场贴标签，并说明为什么不是简单看名气/赔率]

## 📋 二、赛前信息表
| 项目 | 信息 |
| --- | --- |
| 赛事/时间 | [赛事 + 北京时间] |
| 场地/天气 | [场地 + 天气；未确认则写未确认] |
| 中国足彩玩法 | [竞彩足球/传统足彩 + 具体玩法] |
| 关键伤停 | [中文译名 + 状态] |
| 信息时间 | [YYYY-MM-DD HH:mm 时区] |

## 🧠 三、预测理由
🔥 主队状态与火力：[2-3 句，近期表现和进攻/防守趋势]
🧊 客队状态与抗压：[2-3 句，近期表现、防守韧性、反击质量]
🚑 伤停与阵容：[2-3 句，关键球员中文译名、确认/疑问状态]
⚔️ 战术对位：[2-3 句，本场最关键的攻防点]
🧱 阵容厚度：[2-3 句，排名、身价、联赛质量、核心球员层级]
🗓️ 战意赛程：[2-3 句，战意、休息、旅途、赛程压力]

## 📊 四、竞彩赔率与概率
玩法：[胜平负/让球胜平负/总进球数/比分/半全场/混合过关]
当前赔率：[x.xx]
市场去水概率：[x%]
我的估计概率：[x%]
公允赔率：[x.xx]
价值判断：[有正向空间/赔率偏低/暂不推荐]

## ⚽ 五、进球与比分预测
[3-5 句，用总进球数和比分玩法表达，不写非中国足彩市场]

## 🧩 六、比赛脚本推演
- 正向脚本：[推荐最容易命中的比赛路径]
- 中性脚本：[推荐仍可能命中的胶着路径]
- 反向脚本：[推荐失效的比赛路径]

## 🌦️ 七、场外因素
[天气、场地、裁判、旅途等；未确认则明确不纳入主判断]

## ⚠️ 八、最大风险
[写清楚 1-2 个会导致判断失效的比赛脚本]

## 📝 九、信息缺口
[列出未确认数据及其可能改变的结论；没有缺口则写“仍需临场复核首发和赔率”]

## ✅ 十、最终推荐卡
比赛：[主队] vs [客队]
主推：[竞彩玩法 + 方向]
次选：[可选]
玩法：[胜平负/让球胜平负/总进球数/比分/半全场/混合过关]
方向：[推荐方向]
信心：[A/B/C｜星级]
定位：[主推/次选/谨慎/暂不推荐]
比分参考：[1-3 个小范围比分]
总进球数参考：[0/1/2/3/4/5/6/7+]

赛前信息会变，临场阵容和赔率变化需要复核；以上是概率判断，不是收益承诺。
```

### 小红书版（默认）

Best for social notes. Use the fixed Qianwen-style emoji template below by default; it should feel like a readable Xiaohongshu football note with a strong conclusion, rich subpoints, and visible China-lottery risk discipline.

Depth requirements for one match:

- Use exactly these 6 major sections in this order unless the user explicitly asks for another style or a shorter answer: `🎯 预测结论`, `⚖️ 比赛定性`, `🧠 预测理由`, `⚽ 进球预测`, `🌦️ 场外因素`, `✅ 总结`.
- The `🎯 预测结论` section must start with the compact decision table. Keep the table columns exactly as shown below, and include at least 3 rows in the separate `风险档位` column: `稳健档`, `平衡档`, and `博高赔`, ordered from lower risk/lower potential odds return to higher risk/higher potential odds return. Keep the `推荐` cell clean with only the China-lottery pick direction, such as `让平`, `负`, or `比分 1-2/0-2`; do not repeat the risk tier inside `推荐`. Do not include `价值判断` or `主要风险` as table columns; explain value and risk in the paragraph after the table plus the later `竞彩赔率与概率` and `总结` content.
- Each major section body must contain at least 100 Chinese characters. The table header, table separators, and section heading do not count toward the 100-character body requirement.
- Target roughly 1,800-2,800 Chinese characters for a normal single-match note. If a source is unavailable, write what is missing, why it matters, and whether confidence should be downgraded.
- `🧠 预测理由` must be split into numbered emoji subpoints; do not compress it into one paragraph. `🌦️ 场外因素` must also be split into exactly 5 numbered emoji subpoints, matching the style of `预测理由`; do not output it as one combined paragraph, and do not invent weather, referee, or travel facts without a source.

```text
🎯 预测结论
| 风险档位 | 比赛 | 竞彩玩法 | 推荐 | 信心 | 估计概率 | 公允赔率 | 当前赔率 | 核心理由 |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | --- |
| 稳健档 | [主队] vs [客队] | [低风险中国足彩玩法，如让球胜平负/胜平负/总进球数稳健区间] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |
| 平衡档 | [主队] vs [客队] | [中风险中国足彩玩法，如胜平负/总进球数/半全场稳健组合] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |
| 博高赔 | [主队] vs [客队] | [高风险中国足彩玩法，如比分/半全场/更窄总进球数] | [方向] | [A/B/C｜星级] | [x%] | [x.xx] | [x.xx] | [一句话概括最关键的推荐理由] |

[至少100个中文字符。表格后必须再写一段强结论：先说明三档推荐的风险和潜在赔率回报为什么依次加大，再写本场主推什么、次选什么、比分参考和总进球数参考是什么。语气可以有观点，但不能写确定性推单词；要说明这不是简单追热门，也不是无依据搏冷，而是基于中国竞彩赔率、球队状态、阵容信息和反向风险后的赛前概率判断。]

⚖️ 比赛定性
[至少100个中文字符。参考千问模板，用一句有记忆点的话给比赛贴标签，例如强弱分明、热门过热、让球陷阱、拉锯防冷、进球数低开高走。随后交代赛事背景、比赛时间地点、双方定位、市场容易误判的点、主推荐最需要满足的比赛节奏，以及为什么不能只看排名、名气或当前赔率下结论。]

🧠 预测理由
1. 🔥 状态火力：[至少2-3句。写双方近期走势、进攻效率、防守稳定性、样本对手质量、核心球员状态，球员名必须使用中文球迷常用译名。]
2. 🚑 伤停阵容：[至少2-3句。写确认缺席、出战成疑、停赛、轮换风险，说明影响的是边路推进、中场控制、定位球、防线默契还是终结效率。]
3. ⚔️ 战术对位：[至少2-3句。写边路/中路攻防、压迫与反压迫、转换进攻、定位球、身后空间，并把战术点连接到竞彩推荐方向。]
4. 📈 阵容厚度：[至少2-3句。写排名、身价、联赛质量、替补深度、核心位置层级差，不要只说强弱，要说明强在哪里、弱队能靠什么抵抗。]
5. 🗓️ 战意赛程：[至少2-3句。写积分/小组形势、杯赛优先级、休息天数、旅途消耗、连续作战和临场战意。]
6. 📊 竞彩赔率与概率：[至少2-3句。只使用中国足彩玩法口径，写当前赔率、市场去水概率、我的估计概率、公允赔率、价值判断和临场赔率阈值。不能把亚盘、大/小球、球员道具作为最终推荐。]

⚽ 进球预测
[至少100个中文字符。把进球判断映射到中国竞彩 `总进球数` 的 0/1/2/3/4/5/6/7+ 和 `比分` 玩法。说明最可能的进球路径，例如定位球、边路传中、反击、二点球或高压失误；再写先进球后的节奏变化、最可能比分区间、冷门比分触发条件。比分只能作为参考，不能替代主推荐。]

🌦️ 场外因素
1. 🌧️ 天气场地：[至少1-2句，必须单独成点。有来源才写天气、温度、风雨、草皮和场地条件；未确认则写“未确认，不纳入主判断”，并说明可能影响进球数、对抗节奏还是传控质量。]
2. 🧳 旅途时差：[至少1-2句，必须单独成点。写跨洲飞行、休息天数、连续客场、赛程密度和适应问题；没有可靠信息时说明缺口，不要脑补。]
3. 👨‍⚖️ 裁判尺度：[至少1-2句，必须单独成点。只有可靠来源时才写犯规、点球、红黄牌倾向及其对比赛节奏的影响；无来源则明确不纳入主判断。]
4. 🏟️ 主客氛围：[至少1-2句，必须单独成点。写主场、中立场、观众结构、草皮熟悉度和心理压力，对节奏、压迫、防守稳定性或反击效率的影响。]
5. 📝 信息缺口：[至少1-2句，必须单独成点。列出首发、赔率、天气、伤停中仍需临场复核的内容，并说明哪些变化会让推荐降级或转向暂不推荐。]

✅ 总结
[至少100个中文字符。先用一句话收束本场核心判断，然后固定输出最终推荐卡：比赛、主推、次选、比分参考、总进球数参考、定位、信息时间、临场复核点。必须写最可能打穿推荐的反向路径，例如热门早早进球后节奏失控、弱队红牌、主队边路被打穿、临场核心缺席、赔率大幅下调等。最后补一句风险提示：这是赛前概率判断，不是收益承诺，临场首发和赔率变化要重看。]
```

### Risk Note

```text
以上是赛前信息下的概率判断，不是收益承诺。临场阵容、赔率和天气变化会改变结论；若关键数据无法确认，本场应降级或放弃。
```
