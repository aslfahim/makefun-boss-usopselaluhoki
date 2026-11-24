# One Word for the Boss — Legend

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-usopselaluhoki/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-usopselaluhoki/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on [make.fun](https://make.fun).

## The word

**Legend.**

Every office has one: the boss whose stories get retold at lunch long
after the meeting ended — the impossible deadline they somehow landed,
the client they won over with one phone call, the time they showed up
at 2 a.m. to help finish the job. Nobody says "my manager" with that
kind of grin. They say "my boss is a legend."

That is why "Legend" is the funniest and truest single word for a boss.
It is funny because it is slightly too grand for the person who signs
your leave forms, and it is true because the best bosses really do
become office folklore. It needs no caption, no explanation, and no
industry to make sense — a kitchen, a warehouse, or an office all have
a legend in charge. It is the word colleagues repeat, not the word
anyone reaches for first, which is exactly what makes it land.

## How it works

`main.py` (Python 3 standard library only, no third-party imports)
writes exactly the word `Legend` — six bytes, no trailing newline,
no punctuation — to `entry.txt` inside the output directory
(`OUTPUT_DIR` environment variable, default `/output`).

Before writing, it validates the word: 1–30 characters, a single word
with no whitespace and no punctuation. After writing, it reads the
file back and only exits successfully when the bytes on disk match
the word exactly.

## How to run it

```sh
OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt   # Legend
```
