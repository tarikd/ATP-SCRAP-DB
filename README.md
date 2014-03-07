# ATP SCRAP DB
------------

I'm trying to build a scrapper that will allow me to create a database of all the ATP tournaments since 1996.

I will display for each round, every match with the names of the two players and their rank at that moment, the winner of the match and the score.


I have to get the ranks from an other part of the ATP website which increases my script complexity and runtime.

To scrap all the finals of the Grand Chelem tournaments since 1996, the script needs 30 min if run with [PyPy](http://pypy.org/).

You get for Roland Garros Final :

```
US Open
NY, U.S.A.
Hard

ANNEE           PRIZEMONEY      TOUR            RANK1 JOUEUR1                   RANK2 JOUEUR2                   GAGNANT                   SCORE

26.08.1996      $4,806,000      Final Round     1     Sampras, Pete             3     Chang, Michael            Sampras, Pete             6-1, 6-4, 7-6(3)
25.08.1997      $5,152,000      Final Round     20    Rusedski, Greg            14    Rafter, Patrick           Rafter, Patrick           6-3, 6-2, 4-6, 7-5
31.08.1998      $6,032,000      Final Round     3     Rafter, Patrick           22    Philippoussis, Mark       Rafter, Patrick           6-3, 3-6, 6-2, 6-0
30.08.1999      $6,257,000      Final Round     7     Martin, Todd              2     Agassi, Andre             Agassi, Andre             6-4, 6-7(5), 6-7(2), 6-3, 6-2
28.08.2000      $6,834,415      Final Round     4     Sampras, Pete             7     Safin, Marat              Safin, Marat              6-4, 6-3, 6-3
27.08.2001      $6,382,000      Final Round     4     Hewitt, Lleyton           10    Sampras, Pete             Hewitt, Lleyton           7-6(4), 6-1, 6-1
26.08.2002      $7,129,000      Final Round     6     Agassi, Andre             17    Sampras, Pete             Sampras, Pete             6-3, 6-4, 5-7, 6-4
25.08.2003      $7,586,000      Final Round     3     Ferrero, Juan Carlos      4     Roddick, Andy             Roddick, Andy             6-3, 7-6(2), 6-3
30.08.2004      $7,946,000      Final Round     1     Federer, Roger            5     Hewitt, Lleyton           Federer, Roger            6-0, 7-6(3), 6-0
29.08.2005      $7,950,000      Final Round     1     Federer, Roger            7     Agassi, Andre             Federer, Roger            6-3, 2-6, 7-6(1), 6-1
28.08.2006      $8,332,000      Final Round     1     Federer, Roger            10    Roddick, Andy             Federer, Roger            6-2, 4-6, 7-5, 6-1
27.08.2007      $8,848,000      Final Round     1     Federer, Roger            3     Djokovic, Novak           Federer, Roger            7-6(4), 7-6(2), 6-4
25.08.2008      $9,350,000      Final Round     6     Murray, Andy              2     Federer, Roger            Federer, Roger            6-2, 7-5, 6-2
31.08.2009      $9,756,000      Final Round     1     Federer, Roger            6     Del Potro, Juan Martin    Del Potro, Juan Martin    3-6, 7-6(5), 4-6, 7-6(4), 6-2
30.08.2010      $10,508,000     Final Round     1     Nadal, Rafael             3     Djokovic, Novak           Nadal, Rafael             6-4, 5-7, 6-4, 6-2
29.08.2011      $10,768,000     Final Round     1     Djokovic, Novak           2     Nadal, Rafael             Djokovic, Novak           6-2, 6-4, 6-7(3), 6-1
27.08.2012      $11,777,000     Final Round     4     Murray, Andy              2     Djokovic, Novak           Murray, Andy              7-6(10), 7-5, 2-6, 3-6, 6-2
26.08.2013      $16,102,000     Final Round     1     Djokovic, Novak           2     Nadal, Rafael             Nadal, Rafael             6-2, 3-6, 6-4, 6-1
```

# Improvement to come
---------------------

There is still room for improvement especially on the runtime front.
I will put in place a dictionary to store the weekly top300 ranking since 1996. This will allow the script to run faster without scrapping each time the same pages.

I have to adapt the script to the ATP Master1000 because of the difference in the number of contestant during the first round.

...