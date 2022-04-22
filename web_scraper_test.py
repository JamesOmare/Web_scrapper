from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    doc = BeautifulSoup(file, "html.parser")

# print(doc.prettify())

# tag = doc.title
# print(tag)
# print(tag.string)
# tag.string = "hello"
# print(doc)

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

