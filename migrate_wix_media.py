#!/usr/bin/env python3
from pathlib import Path
import urllib.request, urllib.error
import time, sys

ROOT = Path(__file__).resolve().parents[1]
MEDIA = {
    "assets/images/home/site-graphic.png": "https://static.wixstatic.com/media/31aed3_f080e02497004ebdb4f0f1cc5b92d018~mv2.png/v1/fit/w_395%2Ch_298%2Cq_90%2Cenc_avif%2Cquality_auto/31aed3_f080e02497004ebdb4f0f1cc5b92d018~mv2.png",
    "assets/images/home/profile.jpg": "https://static.wixstatic.com/media/31aed3_d42f0ae60c534d51b2e7580da1091eb2~mv2.jpg/v1/fill/w_252%2Ch_447%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_d42f0ae60c534d51b2e7580da1091eb2~mv2.jpg",

    "assets/images/fan/hero.jpg": "https://static.wixstatic.com/media/31aed3_de28208e7020487da252b6d72be098a0~mv2.jpg/v1/fill/w_595%2Ch_446%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_de28208e7020487da252b6d72be098a0~mv2.jpg",
    "assets/images/fan/lcd.png": "https://static.wixstatic.com/media/31aed3_9d83342fd8dc4bce9d821237a2130ae8~mv2.png/v1/fill/w_442%2Ch_258%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/0bc0b47d-6ee7-473a-96ed-fe407e0a26de_rw_600%20%281%29.png",
    "assets/images/fan/detail.png": "https://static.wixstatic.com/media/31aed3_5aeede1766ba4e3fab1a068267c7fedb~mv2.png/v1/fill/w_435%2Ch_253%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_5aeede1766ba4e3fab1a068267c7fedb~mv2.png",
    "assets/images/fan/completed.jpg": "https://static.wixstatic.com/media/31aed3_57b2a21363fc4f7398f29a6abf043828~mv2.jpg/v1/fill/w_449%2Ch_253%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_57b2a21363fc4f7398f29a6abf043828~mv2.jpg",

    "assets/images/coin-counter/hero.jpg": "https://static.wixstatic.com/media/31aed3_8a1b8a43ea6941a58a94b050480d4936~mv2.jpg/v1/fill/w_595%2Ch_446%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_8a1b8a43ea6941a58a94b050480d4936~mv2.jpg",
    "assets/images/coin-counter/lcd.jpg": "https://static.wixstatic.com/media/31aed3_d22bee321c624c988d6cb087fdc6d53e~mv2.jpg/v1/fill/w_414%2Ch_233%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_d22bee321c624c988d6cb087fdc6d53e~mv2.jpg",
    "assets/images/coin-counter/schematic.png": "https://static.wixstatic.com/media/31aed3_4c25af3297254e968768abacecb27bdc~mv2.png/v1/fill/w_420%2Ch_332%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_4c25af3297254e968768abacecb27bdc~mv2.png",

    "assets/images/soda-machine/hero.jpg": "https://static.wixstatic.com/media/31aed3_f138cf08c4fd4224ae1b88d71a35dc2f~mv2.jpg/v1/fill/w_595%2Ch_446%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_f138cf08c4fd4224ae1b88d71a35dc2f~mv2.jpg",
    "assets/images/soda-machine/completed.jpg": "https://static.wixstatic.com/media/31aed3_f7a0198d9157487e9a46b3f392449e53~mv2.jpg/v1/fill/w_231%2Ch_412%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/20210510_145245.jpg",
    "assets/images/soda-machine/mobile-control.jpg": "https://static.wixstatic.com/media/31aed3_f9a493842b7a42dab32c4ba77d53e9b3~mv2.jpg/v1/fill/w_600%2Ch_280%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/Screenshot_20221221_210157.jpg",

    "assets/images/rc-car/hero.jpg": "https://static.wixstatic.com/media/31aed3_ae9398b1692d43c0be52c8a31ae804d3~mv2.jpg/v1/fill/w_595%2Ch_446%2Cal_c%2Cq_80%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/31aed3_ae9398b1692d43c0be52c8a31ae804d3~mv2.jpg",
    "assets/images/rc-car/schematic.png": "https://static.wixstatic.com/media/31aed3_912994cc09ed433a997efc9140de3ea4~mv2.png/v1/fill/w_347%2Ch_306%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/1d318c3e-d6a9-4389-9aed-49f46079cd7b_rw_600.png",
    "assets/images/rc-car/drawings.png": "https://static.wixstatic.com/media/31aed3_09332db0c0334226b559ec5af6647afa~mv2.png/v1/fill/w_375%2Ch_273%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto/8575965b-e9e5-46eb-bd9e-92d85d007d60_rw_1200.png",
}

headers = {"User-Agent": "Mozilla/5.0 (GitHub Pages media migration; Ruben Murillo portfolio)"}
failed=[]
for rel,url in MEDIA.items():
    target=ROOT/rel
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and target.stat().st_size > 1024:
        print(f"skip  {rel} ({target.stat().st_size:,} bytes)")
        continue
    print(f"get   {rel}")
    ok=False
    for attempt in range(1,4):
        try:
            req=urllib.request.Request(url,headers=headers)
            with urllib.request.urlopen(req,timeout=45) as r:
                data=r.read()
            if len(data) < 512:
                raise RuntimeError(f"download too small: {len(data)} bytes")
            target.write_bytes(data)
            print(f"      {len(data):,} bytes")
            ok=True
            break
        except Exception as e:
            print(f"      attempt {attempt} failed: {e}")
            time.sleep(2*attempt)
    if not ok:
        failed.append((rel,url))

if failed:
    print("\nFailed downloads:")
    for rel,url in failed:
        print(f"- {rel}\n  {url}")
    sys.exit(1)
print(f"\nMigrated {len(MEDIA)} Wix images into the repository.")
