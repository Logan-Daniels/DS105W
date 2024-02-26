pages = []
for key in menu.keys():
    pages.append(key)
print(pages)

pages = [key for key in menu.keys()]
print(pages)

all_h2_tags = sel.css("h2 ::text").getall()
all_h2_texts = []
for tag in all_h2_tags:
    all_h2_texts.append(tag)
all_h2_texts

all_h2_texts = [tag.get() for tag in sel.css("h2 ::text")]
all_h2_texts