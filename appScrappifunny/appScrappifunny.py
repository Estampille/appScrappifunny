
import urllib.request as ulib
import re
import os


def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()

page = get_html("https://ifunny.co/")
page[:500]

page2=page.decode("utf-8")
page2[:500]

print(len(page))

reg = re.compile('src="(.*?[.]jpg)"')
images = reg.findall(page2)
images[:5]

if not os.path.exists("images/ifunny"):
    os.makedirs("images/ifunny")

for i, img in enumerate(images):
    nom = img.split("/")[-1]
    dest = os.path.join("images/ifunny", nom)
    if os.path.exists(dest):
        continue

    try:
        contenu = get_html(img)
    except Exception as e:
        print(e)
        continue
    print(f"{i+1}/{len(images)}: {nom}")
    with open(dest, "wb") as f:
        f.write(contenu)