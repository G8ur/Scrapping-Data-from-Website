from os import link
from numpy import sort
import requests  #allows to download the html
from bs4 import BeautifulSoup  # use html and grab the data
import pprint # prints is good form
res = requests.get('https://news.ycombinator.com/news')  #gets the requestt from the urll
res2 = requests.get('https://news.ycombinator.com/news?p=2') # from page 2
soup =BeautifulSoup(res.text,'html.parser')
soup2 =BeautifulSoup(res2.text,'html.parser')  #from res2.txt parse the html data that is the data is converted from string to html s that it can work

links = soup.select('.titlelink')   #here .titlelink is the story link and since it is in list form so particular indexing to be done
subtext = soup.select('.subtext')  # all the element with class scoree

links2 = soup2.select('.titlelink')   #here .titlelink is the story link and since it is in list form so particular indexing to be done
subtext2 = soup2.select('.subtext')

mega_links =links +links2
mega_subtext = subtext +subtext2  #combiing the links and subtext of 2 pages

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)  # here the sorting is done on basis of votes as in dictionary theier can be many keys so by using key we do it



def create_custom(links,subtext):
    hn=[]
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points >99:
                hn.append({'title': title, 'link':href,'votes':points})

    return sort_stories_by_votes(hn)
pprint.pprint(create_custom(mega_links, mega_subtext))
# i.e now the only html code will be shown and if we want to access any paricular tag like body then we can do print(soup.body.contents)
# we can also select string being repeated using print(soup.select('a))
# when getting the votes sometimes it is difficult as if some news has no votes then it will give error as it is out of range
