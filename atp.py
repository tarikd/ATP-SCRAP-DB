# coding: utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys
import os

sys.setrecursionlimit(30000)

mon_fichier = open("fichier.txt", "w")

# URL du drawing pour un tournoi une année précise

URL = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e=540&y=2013"


# Fonction qui renvoie le html parsé
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

# Fonction qui récupère le nom du tournoi
def get_tournament_title(section_url):
    soup = make_soup(section_url)
    title = soup.find("a", "tournamentTitle").string
    return title

# Fonction qui récupère le lieu du tournoi
def get_tournament_location(section_url):
    soup = make_soup(section_url)
    location = soup.find("p", "tournamentSubTitle").string.split(" -")[0]
    return location

# Fonction qui récupère la date de début et de fin du tournoi
def get_tournament_date(section_url):
    soup = make_soup(section_url)
    date = soup.find("p", "tournamentSubTitle").string.split("- ")[1]
    debut = date.split("-")[0].encode('utf-8')
    fin = date.split("-")[1].encode('utf-8')
    return debut, fin

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
    list_player_first_round = []
    for name in playerWrap:
        list_player_first_round.append(name.a.string)
        #print name.a.string
    return list_player_first_round


######################################################################################################

# Fonction qui récupère le nom et prénom de tous les gagnants du premier tour
def get_player_name_first_round_winner(section_url):
    soup = make_soup(section_url)
    colonne2 = soup.find("td", "col_2")
    playerWrap = colonne2.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

# Fonction qui récupère le score du match du premier tour
def get_player_score_first_round_winner(section_url):
    soup = make_soup(section_url)
    colonne2 = soup.find("td", "col_2")
    scores = colonne2.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string

######################################################################################################

# Fonction qui récupère le nom et prénom de tous les gagnants du deuxième tour
def get_player_name_second_round_winner(section_url):
    soup = make_soup(section_url)
    colonne3 = soup.find("td", "col_3")
    playerWrap = colonne3.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

# Fonction qui récupère le score du match du deuxième tour
def get_player_score_second_round_winner(section_url):
    soup = make_soup(section_url)
    colonne3 = soup.find("td", "col_3")
    scores = colonne3.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string


######################################################################################################

# Fonction qui récupère le nom et prénom de tous les gagnants du troisième tour
def get_player_name_third_round_winner(section_url):
    soup = make_soup(section_url)
    colonne4 = soup.find("td", "col_4")
    playerWrap = colonne4.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

# Fonction qui récupère le score du match du troisième tour
def get_player_score_third_round_winner(section_url):
    soup = make_soup(section_url)
    colonne4 = soup.find("td", "col_4")
    scores = colonne4.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string



def get_player_name_fourth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne5 = soup.find("td", "col_5")
    playerWrap = colonne5.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

def get_player_score_fourth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne5 = soup.find("td", "col_5")
    scores = colonne5.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string



def get_player_name_fifth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne6 = soup.find("td", "col_6")
    playerWrap = colonne6.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

def get_player_score_fifth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne6 = soup.find("td", "col_6")
    scores = colonne6.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string



def get_player_name_sixth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne7 = soup.find("td", "col_7")
    playerWrap = colonne7.findAll("div", "playerWrap")
    for name in playerWrap:
    	print name.find("a").string

def get_player_score_sixth_round_winner(section_url):
    soup = make_soup(section_url)
    colonne7 = soup.find("td", "col_7")
    scores = colonne7.findAll("div", "scores")
    for score in scores:
    	print score.find("a").string


def get_player_name_seventh_round_winner(section_url):
    soup = make_soup(section_url)
    colonne8 = soup.find("td", "col_8")
    playerWrap = colonne8.findAll("div", "playerWrap")
    for name in playerWrap:
    	return name.find("a").string

def get_player_score_seventh_round_winner(section_url):
    soup = make_soup(section_url)
    colonne8 = soup.find("td", "col_8")
    scores = colonne8.findAll("div", "scores")
    for score in scores:
    	return score.find("a").string

#print get_tournament_title(BASE_URL)
#print get_tournament_location(BASE_URL)
#print get_tournament_date(BASE_URL)
#print get_tournament_surface(BASE_URL)
#print get_tournament_prizemoney(BASE_URL)
#get_player_name_first_round(BASE_URL)

#get_player_name_first_round_winner(BASE_URL)
#get_player_score_first_round_winner(BASE_URL)

#get_player_name_second_round_winner(BASE_URL)
#get_player_score_second_round_winner(BASE_URL)

#get_player_name_third_round_winner(BASE_URL)
#get_player_score_third_round_winner(BASE_URL)

#get_player_name_fourth_round_winner(BASE_URL)
#get_player_score_fourth_round_winner(BASE_URL)

#get_player_name_fifth_round_winner(BASE_URL)
#get_player_score_fifth_round_winner(BASE_URL)

#get_player_name_sixth_round_winner(BASE_URL)
#get_player_score_sixth_round_winner(BASE_URL)

#get_player_name_seventh_round_winner(BASE_URL)
#get_player_score_seventh_round_winner(BASE_URL)



# Expérimentation pour récupérer les paramètres d'un même tournoi pour la période 1996-2013

BASE_URL_YEAR = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e=540&y="

BASE_URL_NAME = "http://www.atpworldtour.com/Share/Event-Draws.aspx?e="

rg = 520

tournamentYear_urls = [BASE_URL_YEAR + str(year) for year in range(1996,2014)]

tournamentName_urls = [BASE_URL_NAME + str(rg) + "&y=2012"]

mon_fichier.write(get_tournament_title(URL)+"\n")
mon_fichier.write(get_tournament_location(URL)+"\n")
mon_fichier.write(str(get_tournament_date(URL))+"\n")
mon_fichier.write(str(get_tournament_surface(URL))+"\n")
mon_fichier.write(str(get_tournament_prizemoney(URL))+"\n")
mon_fichier.write(""+"\n")

mon_fichier.write("Gagnants de " + str(get_tournament_title(URL)) + " de 1996 à 2013"+"\n\n")
mon_fichier.write("Année		Joueurs 				Scores"+"\n\n")

tournamentYear = 1996

for tournamentYear_url in tournamentYear_urls:
	mon_fichier.write(str(tournamentYear) + "		")
	mon_fichier.write(get_player_name_seventh_round_winner(tournamentYear_url)+"			")
	mon_fichier.write(get_player_score_seventh_round_winner(tournamentYear_url)+"\n")
	tournamentYear+=1


mon_fichier.close







