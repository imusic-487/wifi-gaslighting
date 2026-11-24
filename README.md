# One Word for Your Wi-Fi — Gaslighting

[![make.fun bounty](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/imusic-487/wifi-gaslighting/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/imusic-487/wifi-gaslighting/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the make.fun bounty
[One Word for Your Wi-Fi](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
($2, free entry). The program writes one word describing the entrant's
Wi-Fi to `/output/entry.txt`.

## The word

> **Gaslighting**

Full bars, nothing loads — and the router insists everything is fine.
The Wi-Fi tells you you're connected while no page opens, so you start
wondering whether it's you. It is the most recognisable home Wi-Fi
experience there is: not merely slow, but actively lying to you about
being fine. As a network name it works too.

## How it works

`main.py` (Python 3.13, standard library only) reads the word from
`word.txt`, validates it — one word, 1–20 characters, no whitespace —
writes it to `/output/entry.txt` with no trailing newline, then reads
the file back and fails loudly if the bytes differ from the word.

```sh
python3 main.py
# wrote 11 bytes to /output/entry.txt: Gaslighting
```

## Files

- `main.py` — the entrypoint; copies `word.txt` to `/output/entry.txt`
  byte for byte, with validation and read-back verification.
- `word.txt` — the entry word, no trailing newline.
- `LICENSE` — MIT.
