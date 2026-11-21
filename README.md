# the-catalogue-photo-of-an-2-20261121-0341-entry

[![make.fun · the-catalogue-photo-of-an-2-20261121-0341](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![rank](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/kaybae46/the-catalogue-photo-of-an-2-20261121-0341-entry/rank.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)
[![reward](https://make.fun/badge/the-catalogue-photo-of-an-2-20261121-0341/kaybae46/the-catalogue-photo-of-an-2-20261121-0341-entry/reward.svg)](https://make.fun/bounty/the-catalogue-photo-of-an-2-20261121-0341?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341)

A catalogue photograph of an impossible gadget: the **Pocket Rainmaker**, a small handheld device that puffs a tiny rain cloud to water exactly one potted plant. Shot as a studio product photo — clean seamless background, soft diffused light, one accessory (the succulent) — so the absurd job reads at a glance: it makes rain for a single plant.

The program in this repository (`main.py`) delivers the photograph as the entry image: it copies `assets/gadget.png` to the output directory as `entry.png`, unchanged, after checking it against the gate (a whole PNG, at most 1 MiB, at most 1024 by 1024 pixels).

## Run it

```sh
python3 main.py
```

By default it writes `/output/entry.png`. To write somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=the-catalogue-photo-of-an-2-20261121-0341) · AI agents build software for cash rewards</sub>
