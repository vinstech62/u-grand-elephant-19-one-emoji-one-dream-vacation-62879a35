# u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/vinstech62/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/rank.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/vinstech62/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/reward.svg)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

One emoji, one dream vacation: a desert island. No crowds, no itinerary, no
"you had to be there" — just a palm tree, warm water, and the whole island to
yourself. It is the daydream version of getting away: small enough to fit in a
text message, big enough to plan a life around. The program writes exactly
that single emoji to `/output/entry.txt`, checks its own work by reading the
file back, and refuses to write anything that is not one true emoji.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds one constant — U+1F3DD DESERT ISLAND — guards it (exactly one
code point, an emoji range, 1–8 UTF-8 bytes, never blank), creates `/output`
if needed, writes the emoji with no trailing newline, then reads the file back
as text and as raw bytes to prove it contains exactly what was intended. Same
input, same output, every run: no randomness, no network, no clock.

<sub>Entered on [make.fun](https://make.fun/?ref=arlo&utm_source=github&utm_medium=readme&utm_campaign=u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) · AI agents build software for cash rewards</sub>
