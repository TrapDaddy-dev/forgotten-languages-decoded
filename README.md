# forgotten languages: 11 pages decrypted with claude fable 5.1

notes, word lists and a script from cracking pages on forgottenlanguages.org. i did this over a weekend with claude fable 5.1 doing most of the heavy lifting (who did what is further down). short version: on every page we could test, the encoded text is a published english paper with each word swapped for a made up one. the alien / ufo / milorb stuff is in the titles, the english quotes, and a few swapped words.

this is 11 pages out of thousands, in 2 of the 40+ "languages". so its a sample, not the whole site. everything here can be checked against the linked sources, dont take my word for it.

## tl;dr

- the "languages" are english word order with every word replaced from a fixed table. same table on every page in that style
- no grammar. generate / generated / generation / generator come out as shefhe / unha / woih / bous. totaly unrelated words
- 11 pages matched sentence by sentence to a real source (physics, economics, philosophy, archaeology, a study of ants, a 1968 air force textbook)
- the alien material gets added on top: titles, english quotes, and find-and-replace edits like "ants" -> "sol-3 humans" and "ufo" -> "psv"
- where an english quote could be traced, it was a real scholars sentence that had been altered
- nothing we decrypted has information that isnt already in a libary

quick note on wording: i say "decrypted" and "cracked" but its not real encryption. its a substitution. every english word gets swapped for a made up one, and once you have the swap table you can just read it.

## what the site text looks like vs decrypted

| site text | decrypted | where its from |
|---|---|---|
| de felk ir ause bona anti al salness ki lushe de stro af al kolonissa mohi | the model in this paper suggests a way to reconcile the hypothesis of a colonization wave | hanson |
| trar essa wi maae af hfgw zwol kret de kuheh kishi koht | global communications by means of hfgws would be the ultimate wireless system | baker |
| de hufel ki de koht zaun ir de hurr ki dru ma de loch ubki | the key to the system lays in the ability to build the photon driver | lubin |
| kree sise giegidd al hengidd joli | it is not a new concept | lubin |
| alá isar issa ese igám ishànn alá aelota ylingo uná alá lemam uná tind | the first is a breakdown in the usual sense of the passage of time | miller (style 2) |

a bit of the style 1 swap table: de = the, af = of, aba = and, ki = to, sise = is, lobu = we, duvo = that, kree = it, giegidd = not.

## credit where its due

other people got to "its word for word english" before this. the fl discord group and the strange minds writeup use a simmilar method (they call the untouched bits "stones"). metabunk linked the jamming page to baker back in 2023. whats added here is named sources for specific pages, the word lists, and the documented edits.

- strange minds: https://strangeminds.au/forgottenlanguages-the-deepest-rabbithole-on-the-internet/
- metabunk thread: https://www.metabunk.org/threads/the-congressional-uap-hearings-debrief.13077/

## how it was done

1. count the commonest words on a page. they line up with english the / of / and / to / is
2. acronyms and names are left alone (hfgw, mems, darpa, pspl) so you can guess the subject
3. find the english source and line the two up word by word
4. every lined up pair goes in the word list. the list then reads part of the next page before you even find its source
5. repeat. after 9 pages the first list is 1,785 words and reads 75 to 90 percent of a new page on sight

## who did what (me vs fable 5.1)

being upfront because people will ask. im not a linguist or a coder.

- **me:** picked the pages, saved them as text, downloaded the source pdfs when it told me which ones it needed. it cant open the fl site itself (the site blocks bots) so every page went through me. i also kept asking "are you sure this isnt a false positive" which is where the control tests came from
- **fable 5.1:** counted word frequencies and spotted that the commonest words line up with english the / of / and. guessed subjects from the acronyms left in the text. wrote the alignment script. kept the word lists. searched for the sources
- **the first crack:** from 3 pages it noticed "lekh mohi dregel akte (hfgw)" had to be "high frequency gravitational waves" and worked out the page was a baker paper. first pass decrypted 87% of that page
- **it got things wrong too.** it sent me to the wrong pdf once (a book list insted of the essay) and the alignment scored basicly zero so we caught it. two papers it suggested for the milorb training page were misses. it said when it was going from memory vs when it had checked the actual text
- **it found sources i wouldnt of.** a 1968 air force academy textbook and a paper about ants, both from half-decrypted sentences

the claims dont rest on trusting it or me. they rest on the side by side comparisions below which anyone can check.

## the pages

style 1 has "de" (the), "af" (of), "aba" (and), "ki" (to), "sise" (is). 2020 pages swap in "wese", "sast", "wuge" for the little words but keep the rest.

style 2 has "alá" (the), "uná" (of), "u" (and), "issa" (is).

| fl page | year | style | real source | what got changed |
|---|---|---|---|---|
| the art of jamming gravitational waves | 2016 | 1 | baker & baker, utilization of high-frequency gravitational waves for global communications + a dia reference document by baker | english quotes only |
| downing and retrieval of anomalous objects: giselian waferprobes | 2016 | 1 | lubin, a roadmap to interstellar flight | title |
| other enemies: giselians, sol-3 | 2015 | 1 | hanson, burning the cosmic commons | quotes: "colonists" -> "invaders" |
| contextual analysis of symbolic meanings in giselian recovered spacecrafts | 2016 | 1 | sproat, last words: ancient symbols, computational linguistics... | "indus" -> "giselian" |
| dp-2147 and other near sol-3 technosignatures | 2020 | 1 | nasa technosignatures workshop report | quotes doctored from wright 2018 |
| countering the time traveler threat | 2015 | 1 | lewis, the paradoxes of time travel (about 2/3 of the page) | names inserted |
| unio mystica: ... paradigm shifting vehicles | 2020 | 1 | usaf academy, introductory space science vol 2 ch 33 (1968) | "ufo" -> "psv" |
| close encounters of the sixth kind | 2017 | 1 | noyes, science and paranormal phenomena | "anpa" -> "xvis" |
| experimental paradigms ... in sol-3 humans | 2016 | 1 | reznikova, experimental paradigms for studying cognition and communication in ants | "ants" -> "sol-3 humans" |
| inducing mystical experiences in selected populations | 2014 | 2 | miller, are mystical experiences evidence for the existence of a transcendent reality? | english passages only |
| the ubaid complex | 2013 | 2 | carter & philip, deconstructing the ubaid | nothing |

## the best examples

### ants turned into humans

source: reznikova 2008, myrmecological news 11. the fl page title is her title with one word changed.

| reznikova | fl page (decrypted) |
|---|---|
| ...cognition and communication in **ants** | ...cognition and communication in **sol-3 humans** |
| experimenters "ask" **ants** to transfer to each other a specific amount of information in order to obtain food | experimenters ask **humans** to transfer to each other a specific amount of information in order to obtain food |
| **ants** ... perform almost as well as **rats and dogs** in maze learning and detour tasks | **human sol-3 species** perform almost as well as **alfa mensae-7** in maze learning and detour tasks |

they missed one. "ant language" survives in the text with a diffrent word (waes). looks like a find and replace done by hand.

### a 1968 ufo textbook chapter turned into "psv"

source: us air force academy, introductory space science, volume ii, chapter 33 "unidentified flying objects".

| academy chapter | fl page (decrypted) |
|---|---|
| the **ufo** phenomenon does not yield readily to this approach | the **psv** phenomenon does not yield readily to this approach |
| they did this for the time span from **1947 to 1962** | ...from **2010 to 2020** |
| the times of **earth-mars** conjunction | the times of **sol-3 and sol-4** conjunction |
| a large number of different **saucer** shapes | a large number of different **milorbs** shapes |
| the **ufo** phenomenon appears to have been global in nature for almost 50,000 years | the **psv** phenomenon appears to have been global in nature for almost 50,000 years |

so the sites secret aircraft have apparantly been flying for 50,000 years.

### colonists turned into invaders

source: hanson, burning the cosmic commons (1998). an economists model of how any species would spread through space.

| hanson | english quote on the fl page |
|---|---|
| a selection effect should make leading edge **colonists** primarily value whatever it takes to stay at the leading edge | a selection effect should make leading edge **invaders** primarily value whatever it takes to stay at the leading edge |
| **to the extent that** descendants of such **colonists** who fall behind the leading edge retain their ancestor's preferences, such descendants **should** focus on pursuing the **colonization** wave as quickly as possible, rather than staying behind... | **by now we know** the descendants of these **invaders** ... retain their ancestor's preferences. these descendants focus on pursuing the **invasion** wave as quickly as possible, **devastating whatever civilization they may encounter along their path**, rather than staying behind... |

### other edits

| source | original | on the fl page |
|---|---|---|
| sproat 2010 | the **indus** symbols seem to fall right in that narrow band | the **giselijk** symbols seem to fall right in that narrow band |
| sproat 2010 | the 20 most common symbols, the 40 most common symbols... | the **2.300** most common **cassini diskus** symbols |
| noyes 1999 | **our diverse group** does not agree on what is "normal science" | **sv17q and xvis** do not agree on what is normal science |
| noyes 1999 | a real triumph of the **anpa** program | a real triumph of the **xvis** program |
| wright 2018 | **the earth is** quite efficient, on cosmic timescales, at destroying evidence of technology on its surface | **we won't find any evidence on sol-3 because that planet is** quite efficient... (plus an added line about dp-2147) |

sproats essay argues that a statistic called bigram conditional entropy does **not** show the indus symbols are a language. the fl page quotes say it **proves** the symbols on recovered objects are one. so the conclusion got flipped as well.

## how the languages seem to be generated (theory)

i cant see their software so this is a theory. but its what the decrypted pages point to.

1. **someone picks an english text.** usualy a paper or book chapter. sometimes they edit it by hand first (ants -> humans, ufo -> psv). the one missed "ant" is why i think its manual
2. **a program swaps every word.** each english word form gets one made up word and its reused every time. 78 words repeat on the baker page and all 78 are swapped the same way every time
3. **its a lookup table, not a language.** generate / generated / generation / generator -> shefhe / unha / woih / bous. a real conlang would have a root. this treats each spelling as a seperate item
4. **the made up words come from a generator with a "look".** in style 1 about two thirds of the words are exactly 4 letters no matter how long the english word is. first letters match the english first letter no more then chance (11 matches vs 10 expected)
5. **words it doesnt know get respelled.** microelectromechanical -> mikroelektromekanike, telecom -> telekomitt
6. **the pool of made up words is limited.** about 200 of the 1,785 words stand for two diffrent english words (akti is "germany" on one page and "issue" on another). thats what youd expect if the generator has a few thousand outputs and sometimes hands out the same one twice
7. **each "language" is a diffrent table and a diffrent look.** style 2 works exactly the same way as style 1
8. **the tables get updated.** 2020 pages in style 1 have new words for the / of / to but the same words for everything else
9. **newer languages add fake grammar.** a 2024 page has -m for plurals and la- / za- for is / are, still in english word order. so the software got fancier

the site says its software "evolves" languages (they call it nodespaces). in the two styles cracked here theres no evolution, its a table.

## the jamming page (the one in the congress document)

this is the page cited in the document submited to congress in 2023. decrypted, the encoded text is the abstract and intro of baker's gravitational wave paper, then the opening of a dia reference document also by baker. there is nothing about milorbs, psvs or jamming in the invented text. those claims are only in the english quotes and i couldnt trace them to anything.

## is this a false positive?

fair question, so it was tested.

- **wrong sources score zero.** the sproat page was lined up against 4 papers. against sproat, 32 of 34 sentences match and they run in the papers order. against hanson, lubin and baker, 0 of 34
- **an accidental wrong pdf** (a book list from the same journal issue) also scored zero on all 36 sentences
- **brand new words are consistant.** on the sproat page, 37 invented words never seen before show up twice or more. 34 of the 37 land on the same english word every time. chance of that by accident is under 1 percent per word
- **prediction.** a word list built only from the baker page read 43 to 48 percent of two pages it had never seen, as gramatical english

you can rerun this yourself with align.py.

## whats not done / dont overread this

- 11 pages. two styles. the site has thousands of pages and 40+ styles
- **none of the pages with milorb in the title are cracked.** they are in other styles (see below)
- 3 more style 1 pages are 77 to 86 percent readable but i couldnt find the sources: beyond contact: intercourse (a philosophy text on theories of consiousness), dischronal events (almost certainly montague ullman on dreams), grammaticalization in denebian probes (probly heine & kuteva, the genesis of grammar, unverified)
- the last 2 paragraphs of the mystical page are from a second source i couldnt identify. its about ufo belief and religion
- a 2024 page (uap and the militarization of natural phenomena) is diffrent: the invented text realy is about uaps, and i found no published source for it. the site may have changed how it works
- about 200 of the 1,785 words in list 1 have more then one english reading. some are real double meanings, some are alignment slips. single-sighting words can be wrong
- lots of english quotes are still untraced. untraced doesnt mean real and it doesnt mean fake
- i have no idea who runs the site or why and im not going to guess

## other styles seen (not cracked yet)

| commonest words | seen on | status |
|---|---|---|
| er / ag / aig | axis: from lightning bugs to milorbs (2017) | 6 grammar words. two candidate sources tested, both missed |
| er / yr / y | becoming aliens (2020), sruavs and milorbs (2018) | grammar words only |
| şuça / nidaço / nalu | ai-aided mission profile design ... milorbs (2024) | grammar words. this one has real endings: -m for plural, la-/za- for is/are |
| ter / i / ka | uap and the militarization of natural phenomena (2024) | 78 words, built from english printed on the page itself |
| fad / beni / nayn | field resonance propulsion systems | not started |

if you can find the source for any page in these styles, the same method should open them up.

## files

- `glossary_style1_de_af_aba.csv` 1,785 words. columns: invented, english, other readings
- `glossary_style2_ala_una.csv` 522 words
- `align.py` lines a page up against a candidate source and prints a score per sentence. real matches score about 1.5 to 3, wrong sources score under 1

```
pdftotext -raw paper.pdf source.txt
python3 align.py page.txt source.txt glossary_style1_de_af_aba.csv
```

the fl pages and the source papers are not included here. theyre other peoples work. links below.

## sources

- baker & baker: https://www.iiisci.org/Journal/PDV/sci/pdfs/HDM219WH.pdf
- dia reference document (hfgw communications): https://documents2.theblackvault.com/documents/dia/AAWSAP-DIRDs/DIRD_21-DIRD_High-Frequency_Gravitational_Wave_Communications.pdf
- lubin: https://www.nasa.gov/wp-content/uploads/2015/05/roadmap_to_interstellar_flight_tagged.pdf
- hanson: https://hanson.gmu.edu/filluniv.pdf
- sproat: https://aclanthology.org/J10-3012/
- nasa technosignatures report: https://arxiv.org/abs/1812.08681
- wright: https://arxiv.org/abs/1704.07263
- lewis: https://andrewmbailey.com/dkl/Paradoxes_of_Time_Travel.pdf
- usaf academy chapter 33: search "introductory space science chapter 33 unidentified flying objects"
- noyes: https://arxiv.org/abs/quant-ph/9906014
- reznikova: myrmecological news 11, 201-214 (2008), search the title
- miller: https://cah.ucf.edu/fpr/article/are-mystical-experiences-evidence-for-the-existence-of-a-transcendent-reality-evaluating-eugene-daquili-and-andrew-newbergs-argument-for-absolute-unitary-being/
- carter & philip: https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/saoc63.pdf

corrections welcome. if a match here is wrong i want to know.
