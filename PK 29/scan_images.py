import os
import re

dir_path = r"c:\Users\nasar\Downloads\AERO 92\PK 29"
found_imgs = {}

for fname in os.listdir(dir_path):
    if fname.endswith('.html'):
        fpath = os.path.join(dir_path, fname)
        try:
            with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(10000)
                # Find img tags or og:image or favicon or logo or canvas preview
                imgs = re.findall(r'<img[^>]+src=["\']([^"\'>]+)["\']', content, re.IGNORECASE)
                og_imgs = re.findall(r'property=["\']og:image["\'][^>]+content=["\']([^"\'>]+)["\']', content, re.IGNORECASE)
                icons = re.findall(r'rel=["\'](?:shortcut )?icon["\'][^>]+href=["\']([^"\'>]+)["\']', content, re.IGNORECASE)
                
                if og_imgs:
                    found_imgs[fname] = og_imgs[0]
                elif imgs:
                    found_imgs[fname] = imgs[0]
                elif icons:
                    found_imgs[fname] = icons[0]
        except Exception as e:
            pass

print(f"Found image references in {len(found_imgs)} out of {len(os.listdir(dir_path))} files:")
for k, v in list(found_imgs.items())[:20]:
    print(f"  {k} -> {v[:100]}")
