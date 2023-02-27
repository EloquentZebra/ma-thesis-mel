import requests
from bs4 import BeautifulSoup

def getCoop():
	textFile = open("coop.txt", "w")

	# target URL
	base_url = "https://www.taten-statt-worte.ch/de/unsere-taten/tat-nr-"

	# start count
	count = 334

	while (count <= 408):
		# create URL
		url = base_url + str(count) + ".html"
		reqs = requests.get(url)

		# parse HTML
		soup = BeautifulSoup(reqs.text, "html.parser")
		introtext = soup.find("article", {"class": "KBK-005-A-introtext"})

		# write count as index to textfile
		textFile.write(str(count)+";")

		# get title and write to textfile
		titles = introtext.findChildren("h1" , recursive=False)
		for title in titles:
			print("Titel: " + title.get_text())
			textFile.write(title.get_text() + ";")

		# get intro paragraph and write to textfile
		paragraphes = introtext.findChildren("p" , recursive=False)
		for para in paragraphes:
			print("Lead: " + para.get_text())
			textFile.write(para.get_text() + "\n")
			
		# increment
		count = count + 1	

if __name__ == '__main__':
	getCoop()