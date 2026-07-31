# Hemlane Instagram — full run prompt, August 2026

Paste everything below the line into a fresh chat with the `hemlane-instagram` skill loaded.

Two things to have ready before you start:
- **A GitHub fine-grained token** scoped to `alyssa-ctrl/hemlane-social`, Contents Read and write. Paste it when asked. Without it, tiles come to you as files and you drag them into the repo yourself; both routes work.
- **Jacob's master resolution.** Confirm it is at least 1080 tall, or Phase 3 stalls.

**The HeyGen reels are generated fresh in this run**, on the five-look photo avatar pack. An earlier batch (`6240c1cf2f8f4c83a2001df10dffb30e`) rendered the same four scripts on the digital twin and is superseded. Budget 32 credits against 493.

---

Run the Hemlane Instagram engine for **August 2026**, all phases, stopping at each gate.

**Vibe:** builder-to-builder, forward-looking, outcomes measured in dollars.
**Push:** more real customer voice, and lean on the four avatar reels.
Skip the analytics pull this month.

Build and run rather than plan. Batch the work. Self-critique and fix in the same response. Measure compliance, do not assert it. Surface blockers at the end, not inline. When you hit a technical blocker, work around it and say what you did. Governance gates — Dana's sign-off, the evidence standard, fair housing — are not things to work around.

## Authority

`visual-system.md` is visual authority. `voice-and-gates.md` is voice authority. `positioning.md` sets the audience: operators at 10+ units. Never the 1–4 unit hobbyist. Never lead with ease of use or the free plan.

The test before anything ships: can an operator send this to the person who signs off, and look smarter for having sent it?

## Session setup — do this first, none of it survives a reset

```bash
mkdir -p /home/claude/fonts/ttf /home/claude/assets && cd /home/claude/fonts
npm pack @fontsource/inter@latest && tar xzf fontsource-inter-*.tgz
pip install fonttools brotli cairosvg pillow --break-system-packages
python3 -c "
from fontTools.ttLib import TTFont
for w,n in {'400':'Regular','600':'SemiBold','700':'Bold'}.items():
    f=TTFont(f'/home/claude/fonts/package/files/inter-latin-{w}-normal.woff2')
    f.flavor=None; f.save(f'/home/claude/fonts/ttf/Inter-{n}.ttf')"

cd /tmp && curl -sL "https://codeload.github.com/alyssa-ctrl/hemlane-social/tar.gz/refs/heads/main" -o repo.tgz
tar xzf repo.tgz && cp hemlane-social-main/*.jpg /home/claude/assets/

# logo is now IN the repo — fetch, do not regenerate from logo.md
curl -sL "https://raw.githubusercontent.com/alyssa-ctrl/hemlane-social/main/Hemlane_Logo.svg" -o /home/claude/fonts/Hemlane_Logo.svg
python3 -c "
import cairosvg, re
s=open('/home/claude/fonts/Hemlane_Logo.svg').read()
w=re.sub(r'fill=\"#[0-9A-Fa-f]{6}\"','fill=\"#FFFFFF\"',s)
cairosvg.svg2png(bytestring=w.encode(), write_to='/home/claude/fonts/logo_white.png', output_width=1200, background_color=None)
cairosvg.svg2png(bytestring=s.encode(), write_to='/home/claude/fonts/logo_dark.png', output_width=1200, background_color=None)"
```

GT Standard is not licensed here. Inter is the sanctioned fallback. Never Caladea, Trebuchet, or Calibri.

## Traps already found — do not rediscover these

- Repo files are `.jpg`, never `.jpeg`.
- The version of `build_templates.py` in the skill is **not runnable**. It `exec`s a nonexistent `/home/claude/week.py`, points at `/mnt/user-data/uploads/`, uses `.jpeg`, and reads pre-extracted files from `/home/claude/intake/`. Use the repaired copy.
- **Lucas panel is (289, 66) to (949, 726)**, a 660x660 square, then crop (80, 80, 580, 580). The documented (289, 65)–(949, 632) clips 94px off the bottom.
- **`yb` does nothing on 4:3 landscape sources.** At 3200x2400 filling 2160x2700 the height matches exactly. Only portrait sources respond.
- Hero files are re-encodes, 6.8 to 8.8MP, not the 24.5MP the old docs claimed. Fine for feed, nothing survives a hard crop or 4K.
- EXIF orientation is stripped on all fourteen. `exif_transpose` is a no-op. Still call it; do not treat it as a safeguard.
- `IMG_8879_2` is 1024x768. Circular crops only, never full bleed.
- **Raw GitHub URLs take ~30 seconds to propagate**, not a few seconds. Poll until 200. A single fire-and-check reads as failure.
- `api.github.com` is not proxy-blocked; it rate-limits unauthenticated calls. Use codeload or raw for reads.
- The three iPhone clips (IMG_4410, IMG_0382, IMG_0369) are **not** in the repo and are being reshot. Do not plan around them.
- The 640x360 unusable recording lives **inside** Jacob's Descript project. Name-matching on "Recording" grabs the wrong file.
- **The photo avatar looks are cleared.** `production.md` previously said never use the twelve photo_avatar looks on provenance grounds. The operator has confirmed they are built from real footage of her. The five 608x1080 portrait looks are the sanctioned set for this month. Do not revert to the digital twin.

## Phase 0 — Ledger

Assets as a table with clearance states: `yes`, `needs Dana`, `needs consent`, `needs source`. Flag sub-2160px as Story tier. Consent is attested by the operator: anything they uploaded is cleared. Flag only identifiable non-Hemlane faces. **Stop.**

## Phase 1 — Seven-day design gate

**The look is already decided. Reproduce it exactly, do not re-tune.**

| # | Slot | Ground | Source | Parameters |
|---|---|---|---|---|
| 1 | Mon contrarian reel | dark photo | IMG_0373 | `photo_bleed(yb .24, tint .32, br 1.20, scrim .50, amax 224)` |
| 2 | Tue carousel | Aero 100 | IMG_4364 | photo band y644, tint .28, br 1.14 |
| 3 | Wed avatar | dark photo | HeyGen still | placeholder box until Phase 2 |
| 4 | Thu graph | Oxford 600 | none | 217 at Bold 300, blurred slab 300–724 |
| 5 | Fri photo | Turquoise 100 | Lucas | circular 556, corrected panel crop |
| 6 | Sat fun | Turquoise 100 | IMG_8827 | photo band y608, play button |
| 7 | Sun CTA | dark photo | IMG_0288 | `photo_bleed(yb .30, tint .34, br 1.14, scrim .62, amax 238)` |

Type: Bold 80 headlines on 1, 3, 7. Bold 92–94 on 2 and 6. SemiBold 26–30 eyebrows. Regular 26–29 support. 56px outer margin, 8px grid, logo 15% bottom right with 32px padding.

Render all seven, then audit programmatically and report the numbers: dimensions, 8px grid violations, headline sizes against the 66–96 band, logo geometry, distinct source per tile, and mean luminance above the scrim on tiles 1, 3, 7. Render a grid preview. **Stop for sign-off.**

Known and accepted: six of seven templates use three font weights against `visual-system.md`'s max of two, and the Monday and Sunday photo tiles sit below 110 mean luminance. The operator has reviewed both and prefers this look. Do not re-litigate.

## Phase 2 — HeyGen avatar reels

**Generate these four.** Rotate the avatar look each week so the Wednesday slot does not read as the same frame four times.

| Date | Look | Look ID (`avatar_id`) | Script |
|---|---|---|---|
| Aug 5 | Smiling professional, white shirt | `4b7986a3e5cc4ef99314328843a0158c` | AI hard half / thermostat batteries / Jacob's $100 |
| Aug 12 | Professional, navy blue blazer | `b26d272c37854234a2925814166a7fb8` | Automation raised activity, not effectiveness |
| Aug 19 | Professional, gray suit | `d20966fa44a04f71ac67f6d953a99502` | PM companies will not exist in ten years |
| Aug 26 | Smiling professional, grey blazer | `42248b1d7a0d45ca8cc31f679bf945f1` | Renewal process in one head is a dependency |

Spare from the same pack, unused this month: `70e8748c8fe3446e84e038e5db4602f4` (Woman in grey blazer).

All five are `photo_avatar` looks in group `49256bc6eeec4bbaaae6abba0995f2d1`, all support `avatar_v`, all portrait at 608x1080.

Shared config: avatar group `49256bc6eeec4bbaaae6abba0995f2d1`, voice `f5c05aa29c3f4cbcafc5b615c8c43cde`, engine `avatar_v`, 9:16, 1080p, caption `{file_format: srt, style: default}`. Submit as one `create_video_batch`, poll `bulk_video_statuses`.

**Check the first render before trusting the other three.** The source looks are 608x1080 and the output is 1080x1920. Avatar V regenerates rather than scaling the still, so this may be a non-issue, but confirm sharpness on the Aug 5 render before the set is treated as final. The two looks at 2316x3088 (`39228e65612c41b1b70d64bbc4512b06`, `0a092fd8bf374fa7ac7bd0641e0e0386`) are the fallback if quality disappoints.

### The four scripts, verbatim

**Aug 5.** Most of the AI in this industry points at the half that was already easy. The hard half is two in the morning when a pipe goes and nobody is awake. Ours checks the thermostat batteries before it dispatches anyone. Jacob Carroll runs fifteen units and puts a wasted trip at a hundred dollars. This is my avatar. The real Alyssa is with customers.

**Aug 12.** You automated the rent reminders. Delinquency did not move. That is the tell. Automation raises activity, and activity is not effectiveness. The reminder was never the reason people paid late. Find the reason first, then automate the thing that actually moves it. This is my avatar. The real Alyssa is with customers.

**Aug 19.** Property management companies as we know them will not exist in ten years. Not because software replaces them. Because the ones that survive stop selling hours and start selling outcomes, and you cannot sell an outcome you have never measured. Start measuring now. This is my avatar. The real Alyssa is with customers.

**Aug 26.** If your renewal process lives in one person's head, that is not a process. That is a dependency. Portfolios stall at sixty doors for exactly this reason. The fix is boring and it works. Write it down, then let the system run it. This is my avatar. The real Alyssa is with customers.

Every script closes with the disclosure. The container cannot reach the HeyGen CDN, so an overlay cannot be burned in post; putting it in the script is the only route to an on-frame disclosure via the captions. All four deliberately avoid leasing, screening and tenant selection.

Pull a still from each render for that week's Wednesday feed tile. **Stop.**

## Phase 3 — Reels from footage

Pull the transcript from Descript for timecodes, then cut locally with ffmpeg on exact sentence boundaries. Descript is not trusted for compositing or clean cuts and its self-reported success cannot be believed.

Jacob Carroll, Bridging Tenants, 15 units, Minneapolis, managing from San Diego. Project `15f1c042-2b67-4917-97d1-804208187ad4`, drive `bd7c5515-fb65-48b1-acf7-e57f1d75d47d`, composition `8d9b56b2-e3dc-48d6-823c-b1d02fcd0671`. Master is `video1463371490 (2).mp4` at 2280.68s.

Eight cuts per `testimonial-cuts.md`. Branded vertical frame, never a blurred fill. Every in-point on his breath, every out-point after the final consonant plus 300ms. Verify each boundary by ear. Same 2.5s Alyssa CTA card on every clip.

The container cannot fetch Descript URLs. Export the cuts and route them through the repo, which is fine at 20–40s each.

Three usable explainer cuts from project `8eca8d2f-7a60-4aed-8bcc-67f5cd734fa0`: A, B, C. D and E are blocked and need a re-record, not an edit.

**Clip 8 needs Dana** before anything else in the set. **Stop.**

## Phase 4 — Remaining tiles

August 2026 starts on a Saturday. 31 posts:

| Day | Slot | Template | Count | Dates |
|---|---|---|---|---|
| Mon | Contrarian reel | 1 | 5 | 3, 10, 17, 24, 31 |
| Tue | Deep-cut carousel | 2 | 4 | 4, 11, 18, 25 |
| Wed | Avatar reel | 3 | 4 | 5, 12, 19, 26 |
| Thu | Graph | 4 | 4 | 6, 13, 20, 27 |
| Fri | Photo tile | 5 | 4 | 7, 14, 21, 28 |
| Sat | Light reel | 6 | 5 | 1, 8, 15, 22, 29 |
| Sun | CTA | 7 | 5 | 2, 9, 16, 23, 30 |

Pillars: PM 30%, AI 25%, Rates 25%, Founder 20%, rotating on a four-day cycle. Four pillars only, never a fifth.

Distinct source image per tile, no repeats within a block of nine. Render each block of nine as a preview. **Stop.**

## Phase 5 — Captions and Stories

Five-line formula: hook that works alone, three lines of substance, the turn, one action. No hashtags. Keywords woven in.

CTA ladder for the month: Send this to someone 12, Save this 6, Follow for the series 4, Get the report or newsletter 5, Book a demo 3. The demo CTA names Dana and Alyssa and is reserved for 150+ unit operators.

Stories, one a day: reshare with a take 10, poll 8, quiz 6, question box 5, behind the scenes 5. Nineteen need manual posting because stickers cannot be scheduled. Batch them Monday mornings. **Stop. Nothing reaches Ordinal until the operator approves here.**

## Phase 6 — Staging

Ordinal workspace `hemlane`, Instagram connector `d2cc7e13-f54b-4215-9f23-2e0ac584d171`, video label `9c08accf-4438-4991-8e77-f0256e4a5b22`.

Commit tiles to `out/2026-08/`, poll the raw URL until 200, then `ordinal_create_upload` and poll `ordinal_get_upload` until ready before referencing the assetId.

Every post carries `publishAt` at staging: one a day, 09:00 America/Los_Angeles. Dana blocking on every single item, userId `9aff96f6-e55f-498d-8339-5f57f4da72d7`, `isBlocking` true, due `17:00:00Z` two days before that item's publish date. Video first, since it needs no token. Flag the 19 manual Stories.

## Gates — absolute

Operator approves in chat, then Dana approves everything in Ordinal, and that releases it. No outcome claim without a source, a definition, and a denominator. No fabricated customers. Synthetic delivery disclosed on frame. Nothing synthetic near leasing, screening, or tenant selection. Never attribute an adapted idea to a real outside person. Never bash a competitor by name.

**Confirmed:** 105,000+ rentals. 193,000+ maintenance requests. 8,335 eviction cases. 97% kept out of court (Dana gate). 4.8 from 223 Capterra reviews, 217 positive, 4 neutral, 2 negative. 9.9 support at G2. Highest value-for-money in the category per Capterra. No markups on repairs.

**Jacob Carroll, by name:** $100 avoided per prevented dispatch. 19 days to place a tenant, beaten three times of three. Zero vacancy across 15 units.

**Never ship:** "most switched-to platform", any percentage of users who "grow", any AI-generated imagery of people or property, any `ChatGPT_Image_*` file.

**Banned words:** in today's, game-changer, revolutionize, unlock the power of, next level, cutting-edge, best-in-class, industry-leading, seamless, robust, innovative, landscape, ecosystem, journey, navigate, leverage, delve, tapestry. No em-dashes. No rhetorical-question openers. No three-item adjective lists.
