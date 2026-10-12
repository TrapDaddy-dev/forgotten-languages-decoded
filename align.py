#!/usr/bin/env python3
"""align an fl page against a candidate english source.

usage: python3 align.py page.txt source.txt glossary.csv [--learn out.csv]

page.txt     the fl page saved as plain text (invented text + english quotes)
source.txt   the candidate source as plain text (pdftotext -raw works)
glossary.csv invented,english[,other_readings]  (a handful of seed words is enough to start)

prints a score per invented sentence. real matches land around 1.5 to 3.0,
wrong sources sit near 0 to 0.9. with --learn it writes new word pairs that
showed up at least twice with the same english word.
"""
import re, sys, csv, collections, unicodedata

SUFFIX = {'ma', 'la', 'ba', 'mu', 'mi', 'dáliv'}   # second halves of two-piece words
ENG = set('the of and to is that in a we they are it was'.split())

def load_glossary(path):
    g = {}
    for row in csv.reader(open(path, encoding='utf8')):
        if not row or row[0] == 'invented': continue
        words = [row[1]] + (row[2].split(' / ') if len(row) > 2 and row[2] else [])
        g[row[0].replace(' ', '_')] = [w.strip().lower() for w in words if w.strip()]
    return g

def invented(s):
    w = re.findall(r"[^\W\d_]+", s.lower())
    return len(w) >= 4 and sum(x in ENG for x in w) / len(w) < 0.08

def page_sentences(path):
    text = re.split(r'(?i)bibliographica', open(path, encoding='utf8').read())[0]
    out = []
    for line in text.split('\n'):
        for part in re.split(r'"[^"]{40,}"|“[^”]{40,}”', line):
            for s in re.split(r"(?<=[.:?])\s+(?=[A-Z])", part):
                if invented(s): out.append(s.strip())
    return out

def ftok(s):
    out = []
    for x in re.findall(r"[^\W_]+", s.lower()):
        if x in SUFFIX and out: out[-1] += '_' + x
        else: out.append(x)
    return out

def source_tokens(path):
    t = unicodedata.normalize('NFKC', open(path, encoding='utf8').read())
    t = re.sub(r"-\n", "", t)
    t = re.sub(r"\[[\d,\s\-–]+\]", "", t)
    return re.findall(r"[^\W_]+", t.lower())

def align(a, E, G):
    n, m = len(a), len(E)
    prev = [0] * (m + 1); back = []
    for i in range(1, n + 1):
        x = a[i - 1]; g = G.get(x); gs = set(g) if g else None
        cur = [prev[0] - 1] + [0] * m; bk = bytearray(m + 1); bk[0] = 1
        for j in range(1, m + 1):
            y = E[j - 1]
            if x == y: s = 3
            elif gs is None: s = 0.3
            elif y in gs: s = 3
            else: s = -2
            d = prev[j - 1] + s; u = prev[j] - 1; l = cur[j - 1] - 1
            if d >= u and d >= l: cur[j] = d
            elif u >= l: cur[j] = u; bk[j] = 1
            else: cur[j] = l; bk[j] = 2
        back.append(bk); prev = cur
    j = max(range(m + 1), key=lambda j: prev[j]); best = prev[j]; i = n; pairs = []
    while i > 0:
        b = back[i - 1][j]
        if b == 0: pairs.append((a[i - 1], E[j - 1])); i -= 1; j -= 1
        elif b == 1: pairs.append((a[i - 1], None)); i -= 1
        else: j -= 1
    return best, pairs[::-1], j

def main():
    if len(sys.argv) < 4: sys.exit(__doc__)
    G = load_glossary(sys.argv[3]); E = source_tokens(sys.argv[2])
    sents = [ftok(s) for s in page_sentences(sys.argv[1])]
    votes = collections.defaultdict(collections.Counter); res = []
    for rnd in range(2):
        votes.clear(); res = []
        for a in sents:
            best, pairs, pos = align(a, E, G); res.append((best / len(a), pos, pairs))
            if best / len(a) > 1.0:
                for x, y in pairs:
                    if y and x != y and x not in G and not x.isdigit(): votes[x][y] += 1
        if rnd == 0:
            for x, c in votes.items():
                (y, k), tot = c.most_common(1)[0], sum(c.values())
                if k >= 2 and k / tot >= 0.6: G[x] = [y]
    good = sum(s >= 1.5 for s, _, _ in res)
    print(f"{good} of {len(res)} invented sentences match (score >= 1.5)\n")
    for s, pos, pairs in res:
        print(f"[{s:.2f}] @{pos}: " + ' '.join(f"{x}={y or '-'}" for x, y in pairs))
    if '--learn' in sys.argv:
        out = sys.argv[sys.argv.index('--learn') + 1]
        with open(out, 'w', newline='', encoding='utf8') as f:
            w = csv.writer(f); w.writerow(['invented', 'english', 'times_seen'])
            for x, c in sorted(votes.items()):
                (y, k), tot = c.most_common(1)[0], sum(c.values())
                if k >= 2 and k / tot >= 0.6: w.writerow([x.replace('_', ' '), y, k])

if __name__ == '__main__':
    main()
