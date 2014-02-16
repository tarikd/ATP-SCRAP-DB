# coding: utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys

URL = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e=520&y=2013"

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

# Fonction qui récupère le type de surface
def get_tournament_surface(section_url):
    soup = make_soup(section_url)
    inlineWrapper = soup.find("span", "inlineWrapper")
    surface = inlineWrapper.findAll("p")[1] 						
    surface = str(surface).split(">")[3]
    surface = surface.split("<")[0]
    return surface

# Fonction qui récupère la dotation du tournoi
def get_tournament_prizemoney(section_url):
    soup = make_soup(section_url)
    inlineWrapper = soup.find("span", "inlineWrapper")
    prizemoney = inlineWrapper.findAll("p")[2]
    prizemoney = str(prizemoney).split(">")[3]
    prizemoney = prizemoney.split("<")[0]
    return prizemoney



# Fonction qui récupère le nom et prénom de tous les joueurs du premier tour
def get_player_name_first_round(section_url):
    soup = make_soup(section_url)
    colonne1 = soup.find("td", "col_1")
    playerWrap = colonne1.findAll("div", "playerWrap")
    ma_liste = []
    for name in playerWrap:
    	ma_liste.append(name.a.string)
    	#print name.a.string
    return ma_liste

print get_tournament_surface(URL)
print get_tournament_prizemoney(URL)

print len(get_player_name_first_round(URL))



