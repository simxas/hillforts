# Hillforts of Lithuania

Being a medieval era admirer and a history lover in general I decided to do a simple personal project regarding this subject. Since Lithuania has lots of
hillforts around the country I thought it would be nice to create a simple app where I could easily find all the info about any hillfort in country I need, wtih the
ability to clearly see it on the map and so on. There is this website called [piliakalniai.lt](http://www.piliakalniai.lt/about_hillforts.php). It has in fact the list
of all hillforts in Lithuania, but the UI of the website is just... let's say this politely... it is a pain in the ass... the worst part has to be screenshots of maps.
They are so small and without any interaction. See an example here to see what I am talking about: [example](http://www.piliakalniai.lt/piliakalnis.php?piliakalnis_id=110).
As you can see it is very uncomfortable to use.

So I created this app. It contains web scrapping script called `get_data.py` which pulls
the data of >800 hillforts from the website and places that data in to csv file.
To note: website is rendering his content dynamically with Javascript, so I was not able to use Python Beautifulsoup library.

Then there is a script called `all_hillforts_creation.py`. You can use it to create a map of all hilforts in Lithuania.

Next we have `gui.py` and `backend.py` files. Those are for a really simple GUI I developed for myself. You just need
Python 3 and run it with `python3 gui.py`.

Please note that I added my virtual env Requirements.txt file, but in order to use web scrapping script you need to
install additional software for dryscrape. Here is the installation requirements for [dryscrape](http://dryscrape.readthedocs.io/en/latest/installation.html)

Also I'm using Python 3.5.

Also all the generated html files are sitting inside htmls directory :)
