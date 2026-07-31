# The monthly run

Slot-based on purpose. You never decide what format goes where, only what fills it.

## Intake

Three things, once a month.

**Assets**, dumped in any order. I return a ledger for approval:

| Asset | Who is in it | Where | Cleared? |
|---|---|---|---|

Clearance states: `yes`, `needs Dana`, `needs consent`, `needs source`. Nothing enters a slot without one.

**Analytics.** Pull live from Ordinal. Top three, bottom three, follower movement.

**Two lines.** The month's *vibe*, and the *push*, meaning what you want more of than last month. Blank carries over last month's.

## Weekly rhythm

Seven slots repeat. Same seven every week, which is what makes it consistent and fast.

| Day | Slot | Template | Job |
|---|---|---|---|
| Mon | Contrarian reel | 7 cover | Stop the scroll |
| Tue | Deep-cut carousel | 2 | Teach something saveable |
| Wed | Avatar reel | 3 | HeyGen, disclosed |
| Thu | Graph | 4 | One number with a consequence |
| Fri | Photo tile | 1 or 5 | Taste signal, no pitch |
| Sat | Light reel | 6 | The one that actually gets sent |
| Sun | CTA | 7 | The ask |

Roughly 13 reels, 4 carousels, 4 graphs, 4 photo tiles, 5 CTA over 30 days. Pillar rotation runs on a four-day cycle underneath, so nothing clusters and the mix self-balances.

**Protect Saturday.** It looks like the throwaway and it is the slot most likely to out-perform, because sendability beats polish. If a week compresses, cut Thursday.

## Stories

One a day, five types. Story engagement now feeds Feed ranking, so these are load-bearing.

| Type | Per month | Notes |
|---|---|---|
| Reshare with a take | 10 | Amplifies that day's post |
| Poll | 8 | **Manual** |
| Quiz | 6 | **Manual** |
| Question box | 5 | **Manual**, sources next month |
| Behind the scenes | 5 | Tier-two images live here |

Nineteen need manual posting because stickers cannot be scheduled. Batch them Monday mornings.

## CTA ladder

Every post drives an action. Not always a demo, because a feed of demo asks stops being shared.

| CTA | Per month |
|---|---|
| Send this to someone | 12 |
| Save this | 6 |
| Follow for the series | 4 |
| Get the report or newsletter | 5 |
| **Book a demo** | 3 |

The demo CTA names a person. "Book the Leasing Lead and the Team Lead." Reserved for 150+ unit operators. A person converts better than a form, and it is true.

## Gated phases

Stop after each. Do not continue without approval.

**Phase 1 is the design gate and it is not optional.** Build seven days, get the look signed off, then the remaining twenty-three inherit it. Approving one week costs ten minutes. Discovering the look is wrong at post twenty-six costs the month. This is the single most valuable gate in the run.

**Phase 0, Ledger.** Restate the drop as a table with clearance states. Flag sub-2160px as Story tier. Flag EXIF and rotation. **Stop.**

**Phase 1, the seven-day design gate.** Build one complete week: all seven slots, real copy, real images, no placeholders. Render the seven as a single grid preview. This is the look for the whole month. **Stop and get explicit sign-off before anything else is produced.**

**Phase 2, HeyGen avatar reels.** Rotate the five-look photo avatar pack, one look per week, so the Wednesday slot varies across the grid. `avatar_v`, 9:16, 1080p, burned captions, disclosure closing every script. Roughly 8 credits each and a re-render costs the same as an original, so lock scripts first. Look IDs and the rotation are in `production.md`. **Stop.**

**Phase 3, Reels from real footage.** ffmpeg from iPhone clips, the three usable explainer cuts, and the Jacob Carroll testimonial per `testimonial-cuts.md`. Honour rotation flags. **Stop.**

**Phase 4, Graphs and static tiles.** Remaining twenty-three, built to the approved week-one look. Render each block of nine as a preview before staging. **Stop.**



**Phase 5, Captions and Stories.** Five-line formula, CTA ladder. Present everything for review. **Stop. Nothing goes to Ordinal until the operator approves it here.**

**Phase 6, Staging.** Only after that approval. Push to Ordinal with `publishAt` already set, one a day at 09:00 America/Los_Angeles, video first since it needs no GitHub token. Attach a blocking Dana approval to every single item, due 17:00:00Z two days before its publish date. Dana's approval is the last action and releases the post automatically. Flag the 19 manual Stories, which she still approves but you post by hand.

## Month end

What published, what slipped, top three and bottom three. That becomes next month's analytics input.
