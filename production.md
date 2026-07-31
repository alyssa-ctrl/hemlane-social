# Production

How to actually make the assets. Reproduce, do not reinterpret. Prose has failed to produce a consistent render three times in this project; this file plus `assets/build_templates.py` is the correction.

*Verified against live connectors and the asset repo on 31 July 2026. Changed sections are marked.*

## Fonts

GT Standard is the brand face and is not licensed here. Inter is the sanctioned fallback.

```bash
npm pack @fontsource/inter@latest && tar xzf fontsource-inter-*.tgz
pip install fonttools brotli --break-system-packages
# convert package/files/inter-latin-{400,600,700}-normal.woff2 to ttf, fontTools, flavor=None
```

Caladea sits at `/usr/share/fonts/truetype/crosextra/` and is **retired**. Do not use it.

## Logo

`assets/Hemlane_Logo.svg`. Rasterise with cairosvg at width 1200. White variant for dark grounds, as-is for light. Place bottom-right at 15% of canvas width, 32px padding.

**The SVG is not in the asset repo.** Write it to disk from the source block in `logo.md` at the start of every session. Never recreate it by hand.

## The seven templates

`assets/build_templates.py` renders all seven at 1080x1350, 2x supersampled. **Change copy and source images. Do not rewrite the layout.**

**The script in the project was not runnable and has been repaired.** Four faults, all fixed in the current version:

- line 46 `exec(open('/home/claude/week.py')...)` referenced a file that does not exist. The script was a fragment stitched from two sources. It is now self-contained.
- `U="/mnt/user-data/uploads/"` pointed at chat uploads. Assets come from the repo checkout, now `A="/home/claude/assets/"`.
- source images were referenced as `.jpeg`. Every file in the repo is `.jpg`.
- `lucas()` and the Saturday frame read `/home/claude/intake/...`, pre-extracted files that never existed in a fresh session. Both are now derived inline.

**Session setup, in order.** Fonts, then logo, then assets, then render. None of the three prerequisites survive a session reset:

```bash
# fonts -> /home/claude/fonts/ttf/Inter-{Regular,SemiBold,Bold}.ttf
# logo  -> /home/claude/fonts/logo_{white,dark}.png  (from logo.md, via cairosvg)
curl -sL "https://codeload.github.com/alyssa-ctrl/hemlane-social/tar.gz/refs/heads/main" -o repo.tgz
tar xzf repo.tgz && cp hemlane-social-main/*.jpg /home/claude/assets/
python3 build_templates.py
```

Locked: Denim tint 30 to 38%, saturation 1.40 to 1.45, brightness 1.12 to 1.22, foot scrim Oxford 600 from 46 to 62% height, 8px grid, 56px outer margin.

| # | Template | Ground | Notes |
|---|---|---|---|
| 1 | Photo tile | Dark, photo | Bright photo, Aquamarine head, Mint support |
| 2 | Carousel cover | Bright Aero | Promise on slide one, photo band below |
| 3 | Avatar | Dark, photo | Disclosure line on frame |
| 4 | Graph | Oxford 600 | The number **is** the graph. Blurred slab for depth |
| 5 | Team photo | Bright Turquoise | Circular crop, real person |
| 6 | Fun reel | Bright Turquoise | Biggest type in the set, play button |
| 7 | CTA | Dark, photo | Photo-led, face, one line |

**Template 3 currently upscales a Story-tier file.** It runs IMG_8879_2 (1024x768) full bleed at 1080x1350. That is an upscale on a feed tile and cannot ship as built. The HeyGen still replaces it at Phase 2, which is what the on-frame placeholder box is for.

## Asset source **[CHANGED]**

Assets live in the public GitHub repo `alyssa-ctrl/hemlane-social`, branch `main`.

**Reading needs no token.** `github.com`, `codeload.github.com` and `raw.githubusercontent.com` are all on the container allowlist. Pull the whole tree in one call:

```bash
curl -sL "https://codeload.github.com/alyssa-ctrl/hemlane-social/tar.gz/refs/heads/main" -o repo.tgz
tar xzf repo.tgz
```

`api.github.com` is **not** proxy-blocked. The 403 previously recorded here was GitHub rate-limiting unauthenticated requests from the shared container IP:

> API rate limit exceeded for 35.239.245.65

Unauthenticated reads should still go via codeload or raw to avoid burning quota, but the API is reachable and an authenticated call would work.

**Writing does not need a token, and the standing decision is not to use one.** Finished tiles are presented as files at the end of each phase and the operator drags them into the repo through GitHub's web UI. Ordinal then fetches them from the public raw URLs exactly as it would have. No credential enters the session.

Raw URL shape, for `ordinal_create_upload`:

```
https://raw.githubusercontent.com/alyssa-ctrl/hemlane-social/main/<path>
```

Commit finished tiles under `out/<month>/`, so August week one is `out/2026-08/1_MON_reel.jpg`. Wait for the raw URL to 200 before referencing it; propagation is a few seconds.

## Image inventory **[CHANGED]**

The repo copies are re-encodes, not camera originals. The megapixel figures previously recorded in this file described the originals and are wrong for the files we actually build from. Actual, measured:

| File | Actual pixels | MP | Orientation |
|---|---|---|---|
| IMG_0288 | 3200x2400 | 7.7 | upright |
| IMG_0373 | 3200x2400 | 7.7 | upright |
| IMG_0134 | 2400x3200 | 7.7 | upright |
| IMG_2204 | 2400x3200 | 7.7 | upright |
| IMG_5847 | 3200x2752 | 8.8 | upright |
| IMG_0407 | 3200x2400 | 7.7 | upright |
| IMG_7946 | 2400x3200 | 7.7 | upright |
| IMG_8821 | 2400x3200 | 7.7 | upright |
| IMG_8827 | 3200x2400 | 7.7 | upright |
| IMG_8843 | 2400x3200 | 7.7 | upright |
| IMG_9206 | 3200x2400 | 7.7 | upright |
| IMG_5156 | 3000x2250 | 6.8 | upright |
| IMG_4364 | 3200x2281 | 7.3 | upright |
| IMG_4396 | 2399x3200 | 7.7 | upright |

**Good enough for feed, not for anything else.** At 2x supersample a 1080x1350 tile renders at 2160x2700. Portrait sources cover that outright. Landscape sources take a 1.125x upscale that disappears on the downsample to final. Nothing here survives a hard crop, a heavy reframe, or any 4K output.

**Story tier, under 2160px:** DanaDunford 1024x1024, Dana__1_ 643x643, IMG_8879_2 (Alyssa) 1024x768, d8164a0c (Lucas) 1238x804, two Facetune files at roughly 1200x800. Circular crops and Stories only.

**Never ship:** any file named `ChatGPT_Image_*`. AI-generated and below feed resolution. None are currently in the repo.

## Rotation and EXIF **[CHANGED]**

**The EXIF traps previously listed in this file no longer exist.** Every hero file in the repo has had its orientation tag stripped and the rotation baked in during re-encode. `ImageOps.exif_transpose` is now a no-op on all fourteen.

Verified by contact sheet on 31 July 2026: all fourteen read upright. The bake was done correctly.

**Keep calling `exif_transpose` anyway.** It costs nothing and protects against a future upload that does carry a tag. But do not treat it as a safeguard that is catching anything today, and do not trust an orientation claim in this file over a contact sheet. Look at the images.

The prior warnings for IMG_0407 (tag 4, vertical flip) and IMG_2204, IMG_7946, IMG_8821, IMG_8843 (rotation flags) are retired. They described the camera originals.

**Lucas is letterboxed. The documented panel coordinates were wrong.** Detection by column and row standard deviation above 60 puts the panel at **(289, 66) to (949, 726)**, a 660x660 square. The previously recorded (289, 65) to (949, 632) clipped 94px off the bottom and pulled a vertically mis-registered crop. Correct sequence: crop the panel at (289, 66, 949, 726), then take (80, 80, 580, 580) of the panel for a centred 500x500. Cropping the raw file grabs the letterbox.

**Video.** IMG_4410 2160x3840 9.2s 4K60. IMG_0382 1080x1920 11.6s. IMG_0369 1920x1080 15.3s. **IMG_0382 and IMG_4410 carry rotation -90.** Honour the display matrix or output is sideways. **None of these three are in the asset repo.** They have to arrive by chat upload or be pushed to the repo before Phase 3.

## HeyGen recipe

| Setting | Value |
|---|---|
| Avatar group | `49256bc6eeec4bbaaae6abba0995f2d1` |
| **Digital twin look, use this** | `0f270cbd60444499abddbdc7061998fc` |
| Default voice | `f5c05aa29c3f4cbcafc5b615c8c43cde` |
| Engine | `avatar_v` |
| Aspect | 9:16 |
| Resolution | 1080p |
| Caption | srt sidecar plus burned `default` style |

**Cost: 8 credits for 20.5 seconds**, roughly 0.4 credits a second. Creator plan carries 493. Four reels a month is about 32, under 7%. Cost is not the constraint. **Re-renders are.** A regeneration costs the same as the original, so lock the script before generating.

**Photo avatar looks: provenance confirmed, cleared for use.** The prior instruction here said never use the twelve photo_avatar looks, on the grounds of generic names and unverified provenance. The operator confirmed on 30 July 2026 that they are built from real footage of Alyssa, which resolves the authenticity objection the rule rested on. The auto-generated names ("Professional in gray suit") are cosmetic.

**The sanctioned pack, five portrait looks at 608x1080**, all in group `49256bc6eeec4bbaaae6abba0995f2d1`, all supporting `avatar_v`:

| Look | ID |
|---|---|
| Smiling professional, white shirt | `4b7986a3e5cc4ef99314328843a0158c` |
| Professional, navy blue blazer | `b26d272c37854234a2925814166a7fb8` |
| Professional, gray suit | `d20966fa44a04f71ac67f6d953a99502` |
| Smiling professional, grey blazer | `42248b1d7a0d45ca8cc31f679bf945f1` |
| Woman in grey blazer | `70e8748c8fe3446e84e038e5db4602f4` |

Rotate the look each week so the Wednesday slot varies across the grid.

**Two higher-resolution looks** at 2316x3088, both named "Photo Avatar": `39228e65612c41b1b70d64bbc4512b06` and `0a092fd8bf374fa7ac7bd0641e0e0386`. Fallback if the 608x1080 sources render soft at 1080x1920.

**Five looks are landscape 1920x1080** and crop badly into 9:16. Do not use for reels: `f54b4af6`, `da2e7ed9`, `c7b70338`, `91e10270`, `3f3433e0`.

**The digital twin** `0f270cbd60444499abddbdc7061998fc` remains valid and is what the superseded batch `6240c1cf2f8f4c83a2001df10dffb30e` used.

Batch with `create_video_batch`, poll with `bulk_video_statuses`. Output URLs stay live about seven days, which is long enough to push into Ordinal without the GitHub token.

## Descript recipe **[CHANGED]**

**What Descript is trusted for:** transcript cuts, Studio Sound, caption generation, single full-frame clip placement.

**What it fails at, repeatedly:** layered compositing, matching demo animation to audio, clean sentence-boundary cuts. It reports success on these and the output is wrong. Its self-reported status cannot be trusted for compositing.

**So the method is:** pull the transcript from Descript for timecodes, then cut locally with ffmpeg on exact sentence boundaries. Descript comes back only for Studio Sound and captions if needed.

**Both drives are now reachable.** `42f3168d-d04a-4856-9abf-a179178503d4` and `bd7c5515-fb65-48b1-acf7-e57f1d75d47d`. The second drive was invisible under the previous authorisation; the account was re-authorised on 31 July 2026 and `get_project` now resolves projects on it. The instruction to move or export anything living on `bd7c5515` is retired.

**The container still cannot reach Descript over the network.** Reauthorising the connector fixed the API, not the allowlist. Consequence: a published Descript URL can be handed to `ordinal_create_upload`, but it cannot be fetched into the container for local ffmpeg work. Any clip that needs the branded vertical frame built locally has to arrive through the GitHub repo or a chat upload. Cut files at 20 to 40 seconds are small enough for the repo; the 38-minute master is not.

**The explainer**, project `8eca8d2f-7a60-4aed-8bcc-67f5cd734fa0`, 113 seconds, Alyssa to camera. Five natural cuts:

| Cut | Timecode | Content | Status |
|---|---|---|---|
| A | 0:00-0:24 | "Most rental softwares are just homework with a login" | **Clean.** Best line in the library |
| B | 0:25-0:44 | Real people and AI behind everything | **Clean** |
| C | 0:45-1:06 | The 2am leak | **Clean**, but caption as how it works, never as a customer story |
| D | 1:07-1:27 | The PM section | **Blocked.** Audio says "Jarvis", which is retired. Cannot be edited out of speech |
| E | 1:28-1:47 | Trust accounts, 105,000, closing | **Blocked.** Audio says "most switched-to platform", which is unsubstantiated |

**Only three of five explainer cuts are usable.** D and E require a re-record, not an edit. Plan around three.

**The testimonial project**, `15f1c042-2b67-4917-97d1-804208187ad4` on drive `bd7c5515`, composition `8d9b56b2-e3dc-48d6-823c-b1d02fcd0671`, 2280.7 seconds. Confirmed reachable.

**Grab the right master.** The project holds three video files. Jacob's master is `video1463371490 (2).mp4` at 2280.68s. There is a duplicate `video1463371490 (2)-1.mp4` at the same duration, and a third file `GMT20260717-195959_Recording_640x360.mp4` at 108.96s which is the unusable 640x360 recording. Name-matching on "Recording" or picking the first video will grab the wrong one.

**Master resolution is still unverified.** `get_project` does not report it. Confirm it is at least 1080 tall before building the vertical frame, because the 16:9 window shrinks and the layout has to be rebalanced if it is not.

**Publishing.** `publish_project` returns a share URL plus a 24-hour public download URL. That download URL feeds `ordinal_create_upload` directly, so Descript video needs no GitHub token.

## Ordinal

Workspace `hemlane`. Instagram connector `d2cc7e13-f54b-4215-9f23-2e0ac584d171`. Video label `9c08accf-4438-4991-8e77-f0256e4a5b22`. Approval due dates ISO 8601 with `17:00:00Z`, two days before `publishAt`. Paginate with the last returned post ID as `cursor`. Analytics via `ordinal_get_analytics` with `type: posts`.

Attachment needs a public URL. `ordinal_create_upload` accepts one, then poll `ordinal_get_upload` until ready before referencing the assetId.

## Known contradictions in the brand documents **[NEW]**

Three, surfaced by auditing the rendered week. All need an owner decision; none is safe to resolve silently.

**1. Scrim depth.** `visual-system.md` says darkening is "a short foot scrim only, never a gradient across the whole frame." This file locks the scrim at 46 to 62% of frame height. Sixty-two percent is not a short foot scrim, and the Sunday CTA at 0.62 measured at mean luminance 81 above the scrim, which reads as the buried-photo failure `visual-system.md` explicitly rejects. Sunday now runs at 0.46. **Recommend capping the locked range at 50%.**

**2. Font weights.** `visual-system.md` says max two weights per layout. Six of the seven templates use three: SemiBold eyebrow, Bold headline, Regular support line. The three-tier hierarchy is good typography and the rule is probably what is wrong, but the documents currently contradict each other on every tile except Saturday. **Recommend amending `visual-system.md` to three.**

**3. The photo library does not match the photography direction.** `visual-system.md` calls for "tenants with keys, landlords on site, real interiors with natural light." The fourteen heroes are conference floor, travel, golf, beach and restaurant photographs. They work as people-and-faces content under the SAP model in `growth-playbook.md`, but there is almost no property imagery in the library. **This is a shoot brief, not a doc fix.**

**Brightness floor.** Photo tiles should measure above 110 mean luminance in the region above the scrim. Current week: Monday 147, Wednesday 122, Sunday 174. IMG_0373 (59.7) and IMG_8843 (41.6) are too dark to carry a photo-bleed and should not be used for templates 1, 3 or 7.

**`yb` is a no-op on 4:3 landscape sources.** At 3200x2400 scaled to fill 2160x2700 the height matches exactly, so the vertical crop offset has no effect. Only portrait sources respond to `yb`.

## Network limits

Reachable from the container: GitHub, PyPI, npm, crates. **Not reachable:** iCloud, HeyGen CDN, Descript, Google, Apple. Files from those must arrive as chat uploads or through a connector.

**Consequence.** Video ships to Ordinal without the GitHub token, because HeyGen and Descript both return public URLs that Ordinal can fetch even though the container cannot. Static images cannot reach Ordinal until a fine-grained token scoped to `alyssa-ctrl/hemlane-social` with Contents read and write exists. Local ffmpeg work needs the file in the container, which means GitHub or a chat upload, never a Descript or HeyGen URL.
