# Testimonial cuts: Jacob Carroll

Source: Descript project `15f1c042-2b67-4917-97d1-804208187ad4`, drive `bd7c5515-fb65-48b1-acf7-e57f1d75d47d`. Master `video1463371490 (2).mp4`, 2280 seconds. Composition `8d9b56b2-e3dc-48d6-823c-b1d02fcd0671`.

**Consent:** cleared for publication, confirmed by Alyssa 31 July 2026.

**Who he is:** Jacob Carroll, co-owner of Bridging Tenants. 15 townhouses in the Minneapolis suburbs, self-managed from San Diego, 2,800 miles away. Eight months on Hemlane Complete plus Eviction Shield. On screen he is "Jacob Carroll, Bridging Tenants, 15 units, Minneapolis". Never "a customer".

---

## The vertical treatment

The source is a landscape call recording. **Do not use a blurred fill.** That approach has failed in this project before, dropping the blur layer randomly across cuts.

Build a branded vertical frame instead. Deterministic, no compositing risk, and it looks more considered than a blur.

```
1080 x 1920, Oxford 600 #081326 ground

  y 0    ─ 32px padding
  y 180  ─ eyebrow, Inter SemiBold 30, Mint #BFF8E1
           "Jacob Carroll · Bridging Tenants"
  y 236  ─ subline, Inter Regular 26, Mint 70%
           "15 units, Minneapolis. Managing from San Diego."
  y 470  ─ source clip, 1080 wide, 608 tall (16:9), full width
  y 1090 ─ Aquamarine hairline, 6px, animates left to right as progress
  y 1150 ─ burned captions, Inter Bold 46, white
           keyword words in Aquamarine #23E798
  y 1780 ─ logo, white, 162px wide, bottom right
```

**ffmpeg spine.** Cut on the source first, then compose. Never re-encode twice.

```bash
ffmpeg -ss <IN> -to <OUT> -i master.mp4 -c copy cut_N.mp4
ffmpeg -i cut_N.mp4 -f lavfi -i color=c=0x081326:s=1080x1920 \
  -filter_complex "[0:v]scale=1080:608[v];[1:v][v]overlay=0:470[bg]" \
  -map "[bg]" -map 0:a -c:v libx264 -crf 18 -c:a aac -b:a 192k out_N.mp4
```

Captions burned from the Descript SRT, restyled to Inter. Progress hairline drawn per frame in PIL, overlaid as a PNG sequence.

## The CTA card

Every clip ends with the same 2.5 second card. This is the whole point of the exercise.

```
Primary dark gradient, #081326 → #2661BE → #23E798
Alyssa's photo, circular, 208px, centred at y 620
"Alyssa Clark"                Inter Bold 52, white
"Team Lead, Hemlane"          Inter Regular 30, Mint
"Book 20 minutes."            Inter Bold 72, Aquamarine
"No deck. No SDR. Link in bio."  Inter Regular 28, Mint
logo bottom right
```

Hold 2.5 seconds. Audio ducks to silence over the last 0.4 seconds of speech, no music sting.

---

## The eight cuts

| # | In | Out | Len | Hook line for the caption | Slot | Gate |
|---|---|---|---|---|---|---|
| 1 | 17:39 | 18:00 | 21s | The best thing I ever did for my business was move 2,800 miles away | Mon contrarian | |
| 2 | 16:30 | 17:00 | 30s | You guys are winning because you're not just AI-ing everything | Wed, AI pillar | |
| 3 | 28:26 | 28:52 | 26s | Thirty minutes off the plane, water coming through the ceiling | Sat, pressure | |
| 4 | 19:09 | 19:32 | 23s | Check the battery on your thermostat. That is a hundred dollars saved | Thu, graph pair | |
| 5 | 21:41 | 22:00 | 19s | Three placements, three times under the nineteen day average | Rates | |
| 6 | 27:18 | 27:40 | 22s | What's good isn't cheap, what's cheap isn't good | Sun CTA | |
| 7 | 31:32 | 32:00 | 28s | Every goal measured with a dollar amount attached to it | Rates, spine | |
| 8 | 34:10 | 34:48 | 38s | The one thing Hemlane needs to fix | Founder | |

**Trim discipline.** Every in-point starts on Jacob's breath, not mid-sentence. Every out-point lands after the final consonant plus 300ms. Cut on sentence boundaries only. This is the specific thing the Descript agent gets wrong, so verify each boundary by ear before rendering.

**Clip 2** contains Alyssa's reply about people, AI, and tech being three different answers to three different problems. Keep both voices. The exchange is stronger than either half.

**Clip 8** is the honest-criticism clip. Jacob says the financial accounting needs an overhaul. Publish it with the QuickBooks two-way sync answer in the caption, not edited out. A brand that posts its own weak spot buys trust no positive clip can. It ships with the set; Dana reviews it at staging along with every other item, as she does everything.

---

## Captions, per clip

Five-line formula. Every one ends on the same ask.

**Clip 1.** Jacob ran 15 townhouses in Minneapolis while living in Minneapolis. Then he moved to San Diego. Two thousand eight hundred miles. He says it is the best thing he ever did for the business. Not because distance is good. Because distance forced him to build the system he had been avoiding. Book 20 minutes with Alyssa Clark, Team Lead. Link in bio.

**Clip 2.** We did not write this line. A customer did. Most platforms are answering every problem with AI right now. Some problems want AI. Some want automation. Some want a person to pick up at 2am. Knowing which is which is the entire job. Book 20 minutes with Alyssa. Link in bio.

**Clip 3.** Thirty minutes off the plane in San Diego. Water coming from the second floor to the first, 2,800 miles away. Pressure does not build your process. It shows you whether you had one. Book 20 minutes with Alyssa. Link in bio.

**Clip 4.** A tenant says the heat is out. Before anyone dispatches, the platform asks whether the thermostat has fresh batteries. Sometimes that is the whole repair. Jacob's number for a wasted trip charge is one hundred dollars, and that is before the hourly rate. Book 20 minutes with Alyssa. Link in bio.

**Clip 5.** Three placements through Hemlane, three times under the nineteen day average, zero vacancy across fifteen units. He also says every portfolio is different, which is the honest caveat most case studies leave out. Book 20 minutes with Alyssa. Link in bio.

**Clip 6.** He is not saying we are cheap. He is saying he ran the arithmetic on what his time and his peace of mind were worth, and the number came out in favour. That is the only comparison worth making. Book 20 minutes with Alyssa. Link in bio.

**Clip 7.** Set a goal for the portfolio, then attach a dollar figure to it. Fifteen units to thirty to fifty to a hundred and fifty. Without the number it is a wish. Book 20 minutes with Alyssa. Link in bio.

**Clip 8.** Our accounting is not the best on the market. A customer said it on camera and we are posting it. QuickBooks two-way sync is live, a proper rebuild is on the roadmap, and you should know both before you decide. Book 20 minutes with Alyssa. Link in bio.

---

## Before rendering

1. **Master resolution is 1280x720, verified 30 July 2026.** It downscales cleanly to the documented 1080x608 window, so the frame builds exactly as specified above with no rebalancing. 720p is the ceiling on this footage; captions and the progress hairline are drawn separately at full 1080x1920 and stay sharp. The unusable 640x360 file (`GMT20260717-195959_Recording_640x360.mp4`) sits in the same project, so do not name-match on "Recording".
2. **Verify each boundary by ear.**
3. **Dana approves everything at staging**, this set included. There is no separate pre-flight sign-off for any individual clip.
