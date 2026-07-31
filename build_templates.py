from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import os

# ---- paths -------------------------------------------------------------
I   = "/home/claude/fonts/Inter-%s.ttf".replace("fonts/", "fonts/ttf/")
A   = "/home/claude/assets/"          # repo checkout, was /mnt/user-data/uploads/
OUT = "/home/claude/out/week/"
os.makedirs(OUT, exist_ok=True)

# ---- palette (visual-system.md, nothing outside these families) --------
OX600=(8,19,38); OXD=(9,41,92); DENIM=(38,97,190); DEN700=(30,77,153)
AQUA=(35,231,152); MINT=(191,248,225); WHITE=(255,255,255)
TURQ100=(229,252,251); TURQ500=(51,235,223); TURQ900=(8,84,79)
AERO100=(233,248,252); AERO500=(77,202,233); AERO900=(11,76,93); AQUA800=(20,179,115)

W,H = 1080,1350
S   = 2                                # supersample

def f(w,sz): return ImageFont.truetype(I % w, sz*S)

def logo(im, v="white", pad=32):
    lg = Image.open(f"/home/claude/fonts/logo_{v}.png")
    tw = int(im.width*0.15); th = int(lg.height*tw/lg.width)
    lg = lg.resize((tw,th), Image.LANCZOS)
    im.paste(lg, (im.width-tw-pad*S, im.height-th-pad*S), lg)

def save(im,n):
    im.resize((im.width//S, im.height//S), Image.LANCZOS).save(OUT+n, "JPEG", quality=94)

def tick(d,x,y,c=AQUA,w=56,t=8):
    d.line([(x*S,y*S),((x+w)*S,y*S)], fill=c, width=t*S)

def photo_bleed(p, yb=0.26, tint=0.30, br=1.16, scrim=0.44, amax=232):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    r  = max(W*S/im.width, H*S/im.height)
    im = im.resize((int(im.width*r+1), int(im.height*r+1)), Image.LANCZOS)
    xo = (im.width-W*S)//2; yo = int((im.height-H*S)*yb)
    im = im.crop((xo,yo,xo+W*S,yo+H*S))
    im = ImageEnhance.Color(im).enhance(1.42)
    im = ImageEnhance.Brightness(im).enhance(br)
    im = Image.blend(im, Image.new("RGB",(W*S,H*S),DENIM), tint).convert("RGBA")
    ov = Image.new("RGBA",(W*S,H*S),(0,0,0,0)); od = ImageDraw.Draw(ov)
    top = int(H*S*(1-scrim))
    for y in range(top, H*S):
        od.line([(0,y),(W*S,y)], fill=(8,19,38, int(((y-top)/(H*S-top))**1.4*amax)))
    return Image.alpha_composite(im, ov).convert("RGB")

def slab(im,y0,y1):
    s = Image.new("RGB",(W*S,H*S),OX600); sd = ImageDraw.Draw(s)
    sd.rectangle([0,y0*S,W*S,y1*S], fill=(14,32,62))
    s = s.filter(ImageFilter.GaussianBlur(18))
    im.paste(s.crop((0,(y0-18)*S,W*S,(y1+18)*S)), (0,(y0-18)*S)); return im

def circ(p,sz,br=1.0):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    r  = max(sz/im.width, sz/im.height)
    im = im.resize((int(im.width*r+1), int(im.height*r+1)), Image.LANCZOS)
    im = im.crop(((im.width-sz)//2, 0, (im.width-sz)//2+sz, sz))
    im = ImageEnhance.Color(im).enhance(1.3)
    im = ImageEnhance.Brightness(im).enhance(br)
    m  = Image.new("L",(sz,sz),0); ImageDraw.Draw(m).ellipse((0,0,sz,sz), fill=255)
    return im, m

def lucas(sz):
    # letterboxed source. panel detected at (289,66)-(949,726), not the
    # documented (289,65)-(949,632) which clipped 94px off the bottom.
    p = Image.open(A+"d8164a0c-e171-47a6-9da4-69a9ec52ac57__2_.jpg").convert("RGB")
    p = p.crop((289,66,949,726))
    p = p.crop((80,80,580,580)).resize((sz,sz), Image.LANCZOS)
    p = ImageEnhance.Color(p).enhance(1.32)
    p = ImageEnhance.Brightness(p).enhance(1.08)
    m = Image.new("L",(sz,sz),0); ImageDraw.Draw(m).ellipse((0,0,sz,sz), fill=255)
    return p, m


def play(d, cx, cy, r=56, fill=WHITE, tri=TURQ900):
    d.ellipse([(cx-r)*S,(cy-r)*S,(cx+r)*S,(cy+r)*S], fill=fill)
    d.polygon([((cx-18)*S,(cy-28)*S),((cx-18)*S,(cy+28)*S),((cx+28)*S,cy*S)], fill=tri)

# ---- 1 MON  contrarian reel cover --------------------------------------
im = photo_bleed(A+"IMG_2204.jpg",0.18,0.30,1.18,0.50,224); d = ImageDraw.Draw(im); x = 56
play(d, W//2, 400, 64, WHITE, OX600)
tick(d,x,672); d.text((x*S,700*S),"Renewal season",font=f("SemiBold",28),fill=MINT)
d.text((x*S,768*S),"Rent increases",font=f("Bold",96),fill=WHITE)
d.text((x*S,872*S),"are the lazy",font=f("Bold",96),fill=WHITE)
d.text((x*S,976*S),"lever.",font=f("Bold",96),fill=AQUA)
d.text((x*S,1168*S),"Send this to whoever sets your renewals",font=f("Regular",27),fill=MINT)
logo(im); save(im,"1_MON_reel.jpg")

# ---- 2 TUE  carousel cover ---------------------------------------------
im = Image.new("RGB",(W*S,H*S),AERO100); d = ImageDraw.Draw(im)
d.rectangle([0,0,W*S,14*S],fill=AQUA800); x = 56
tick(d,x,128,AQUA800); d.text((x*S,156*S),"6-part breakdown",font=f("SemiBold",27),fill=AERO900)
d.text((x*S,240*S),"A turn costs",font=f("Bold",94),fill=AERO900)
d.text((x*S,344*S),"more than",font=f("Bold",94),fill=AERO900)
d.text((x*S,448*S),"you think",font=f("Bold",94),fill=AQUA800)
ph = Image.open(A+"IMG_4364.jpg").convert("RGB")
r  = max((W-112)*S/ph.width, 420*S/ph.height)
ph = ph.resize((int(ph.width*r+1),int(ph.height*r+1)), Image.LANCZOS)
ph = ph.crop((0,int(ph.height*0.18),(W-112)*S,int(ph.height*0.18)+420*S))
ph = ImageEnhance.Color(ph).enhance(1.4); ph = ImageEnhance.Brightness(ph).enhance(1.14)
ph = Image.blend(ph, Image.new("RGB",ph.size,DENIM), 0.28); im.paste(ph,(x*S,644*S))
d.text((x*S,1112*S),"Vacancy. Make-ready. Marketing. Screening.",font=f("SemiBold",29),fill=AERO900)
d.text((x*S,1160*S),"Save it before you send that renewal letter",font=f("Regular",27),fill=(17,115,139))
logo(im,"dark"); save(im,"2_TUE_carousel.jpg")

# ---- 3 WED  avatar ------------------------------------------------------
# interim ground. IMG_8879_2 (1024x768) was an upscale and cannot ship.
# HeyGen still replaces this whole frame at Phase 2.
im = photo_bleed(A+"IMG_4396.jpg",0.10,0.30,1.14,0.50,230); d = ImageDraw.Draw(im); x = 56
d.rectangle([x*S,120*S,(x+340)*S,182*S],outline=AQUA,width=4*S)
d.text(((x+20)*S,134*S),"DROP HEYGEN STILL",font=f("SemiBold",24),fill=AQUA)
play(d, W//2, 440, 64, WHITE, OX600)
tick(d,x,736); d.text((x*S,764*S),"AI in property management",font=f("SemiBold",28),fill=MINT)
d.text((x*S,832*S),"AI came for",font=f("Bold",96),fill=WHITE)
d.text((x*S,936*S),"the job nobody",font=f("Bold",96),fill=WHITE)
d.text((x*S,1040*S),"wanted.",font=f("Bold",96),fill=AQUA)
d.text((x*S,1184*S),"Avatar. The real Alyssa is with customers.",font=f("Regular",26),fill=MINT)
logo(im); save(im,"3_WED_avatar.jpg")

# ---- 4 THU  graph -------------------------------------------------------
im = Image.new("RGB",(W*S,H*S),OX600); im = slab(im,300,724); d = ImageDraw.Draw(im); x = 56
tick(d,x,116); d.text((x*S,144*S),"B2B buyers read 11 to 50 reviews first",font=f("SemiBold",26),fill=MINT)
d.text((x*S,264*S),"217",font=f("Bold",336),fill=AQUA)
d.text((x*S,582*S),"of our 223 are",font=f("Bold",70),fill=WHITE)
d.text((x*S,664*S),"positive.",font=f("Bold",70),fill=WHITE)
by,bw,bh = 828, W-2*56, 52
d.rectangle([x*S,(by+8)*S,(x+bw)*S,(by+bh+8)*S],fill=(14,32,62))
d.rectangle([x*S,by*S,(x+int(bw*217/223))*S,(by+bh)*S],fill=AQUA)
d.rectangle([(x+int(bw*217/223))*S,by*S,(x+int(bw*221/223))*S,(by+bh)*S],fill=AERO500)
d.rectangle([(x+int(bw*221/223))*S,by*S,(x+bw)*S,(by+bh)*S],fill=(120,132,150))
d.text((x*S,924*S),"4 neutral. 2 negative. Go read all 223.",font=f("Regular",29),fill=MINT)
d.text((x*S,1048*S),"4.8 on Capterra. 9.9 on support at G2.",font=f("SemiBold",34),fill=TURQ500)
d.text((x*S,1108*S),"Send this to whoever picks your software",font=f("Regular",26),fill=MINT)
logo(im); save(im,"4_THU_graph.jpg")

# ---- 5 FRI  Lucas -------------------------------------------------------
im = Image.new("RGB",(W*S,H*S),TURQ100); d = ImageDraw.Draw(im)
d.rectangle([0,0,W*S,14*S],fill=TURQ500); x = 56
ph,m = lucas(556*S); im.paste(ph,(int((W*S-556*S)/2),148*S),m)
tick(d,x,772,AQUA800); d.text((x*S,800*S),"Lucas, Hemlane",font=f("SemiBold",27),fill=TURQ900)
d.text((x*S,868*S),"Software is",font=f("Bold",84),fill=TURQ900)
d.text((x*S,966*S),"the easy half.",font=f("Bold",84),fill=TURQ900)
d.text((x*S,1064*S),"He is the other half.",font=f("Bold",50),fill=AQUA800)
d.text((x*S,1180*S),"Follow for the people behind the platform",font=f("Regular",27),fill=(12,125,118))
logo(im,"dark"); save(im,"5_FRI_photo.jpg")

# ---- 6 SAT  fun ---------------------------------------------------------
# IMG_4410 frame is missing from the repo. IMG_9206 substituted (IMG_8827 too dark).
im = Image.new("RGB",(W*S,H*S),TURQ100); d = ImageDraw.Draw(im); x = 56
tick(d,x,128,AQUA800); d.text((x*S,156*S),"Things nobody warns you about",font=f("SemiBold",27),fill=TURQ900)
d.text((x*S,232*S),"It is never",font=f("Bold",96),fill=TURQ900)
d.text((x*S,336*S),"the garbage",font=f("Bold",96),fill=TURQ900)
d.text((x*S,440*S),"disposal.",font=f("Bold",96),fill=AQUA800)
fr = Image.open(A+"IMG_9206.jpg").convert("RGB")
r  = max((W-112)*S/fr.width, 480*S/fr.height)
fr = fr.resize((int(fr.width*r+1),int(fr.height*r+1)), Image.LANCZOS)
fr = fr.crop((0,int(fr.height*0.16),(W-112)*S,int(fr.height*0.16)+480*S))
fr = ImageEnhance.Color(fr).enhance(1.45); fr = ImageEnhance.Brightness(fr).enhance(1.2)
fr = Image.blend(fr, Image.new("RGB",fr.size,DENIM), 0.24); im.paste(fr,(x*S,608*S))
play(d, W//2, 848, 56)
d.text((x*S,1148*S),"Tag a PM who has had this week",font=f("SemiBold",30),fill=TURQ900)
logo(im,"dark"); save(im,"6_SAT_fun.jpg")

# ---- 7 SUN  CTA ---------------------------------------------------------
im = photo_bleed(A+"IMG_7946.jpg",0.20,0.32,1.16,0.46,238); d = ImageDraw.Draw(im); x = 56
da,dm = circ(A+"DanaDunford.jpg",188*S,1.10)
al,am = circ(A+"IMG_8879_2.jpg",188*S,1.10)
im.paste(da,(x*S,600*S),dm); im.paste(al,((x+152)*S,600*S),am)
tick(d,x,846); d.text((x*S,874*S),"150+ units",font=f("SemiBold",27),fill=MINT)
d.text((x*S,942*S),"Skip the SDR.",font=f("Bold",78),fill=WHITE)
d.text((x*S,1034*S),"Book the CEO and",font=f("Bold",78),fill=WHITE)
d.text((x*S,1126*S),"the Team Lead.",font=f("Bold",78),fill=AQUA)
d.text((x*S,1244*S),"Dana Dunford and Alyssa Clark. Link in bio.",font=f("Regular",26),fill=MINT)
logo(im); save(im,"7_SUN_cta.jpg")

print("rendered 7 ->", OUT)
