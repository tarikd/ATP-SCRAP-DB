# coding: utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys

mon_fichier = open("fichier.txt", "w")

URL = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e=520&y=2013"

# Fonction qui renvoie le html parsé
def make_soup(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

# Fonction qui récupère le type de surface
def get_tournament_surface(soup):
    inlineWrapper = soup.find("span", "inlineWrapper")
    surface = inlineWrapper.findAll("p")[1] 						
    surface = str(surface).split(">")[3]
    surface = surface.split("<")[0]
    return surface

# Fonction qui récupère la dotation du tournoi
def get_tournament_prizemoney(soup):
    inlineWrapper = soup.find("span", "inlineWrapper")
    prizemoney = inlineWrapper.findAll("p")[2]
    prizemoney = str(prizemoney).split(">")[3]
    prizemoney = prizemoney.split("<")[0]
    return prizemoney



# Fonction qui récupère le nom et prénom de tous les joueurs du premier tour
def get_player_name_first_round(soup):
    colonne1 = soup.find("td", "col_1")
    playerWrap = colonne1.findAll("div", "playerWrap")
    ma_liste = []
    for name in playerWrap:
    	ma_liste.append(name.a.string)
    	#print name.a.string
    return ma_liste

soup = make_soup(URL)

mon_fichier.write(str(get_tournament_prizemoney(soup)))
'{:>30}'.format(mon_fichier.write(str(get_tournament_surface(soup))+"\n"))

mon_fichier.write('{latitude} {lol} {longitude}'.format(latitude=str(get_tournament_prizemoney(soup)), longitude=str(get_tournament_surface(soup))))


#print get_tournament_surface(soup)
#print get_tournament_prizemoney(soup)

#print len(get_player_name_first_round(soup))

#print '{:<30}'.format('left aligned')

