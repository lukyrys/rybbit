import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / 'en.json', encoding='utf-8') as f:
    en = json.load(f)

files = ['cs.json', 'zh.json', 'ja.json', 'de.json', 'pl.json', 'pt.json', 'it.json', 'fr.json', 'ko.json', 'es.json']

has_issues = False

for fname in files:
    with open(BASE_DIR / fname, encoding='utf-8') as f:
        trans = json.load(f)

    empty = [k for k, v in trans.items() if v == '']
    stale = [k for k in trans if k not in en]
    missing = [k for k in en if k not in trans]
    english = [k for k, v in trans.items() if k in en and v == en[k] and v != '']

    if empty or stale or missing:
        has_issues = True

    print(f'{fname}:')
    print(f'  Empty strings: {empty}')
    print(f'  Stale keys: {stale}')
    print(f'  Missing keys: {missing}')
    print(f'  Still English (same as en.json): {english}')
    print()

sys.exit(1 if has_issues else 0)
