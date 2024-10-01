# Python-laboration - Deadline 3/10

## Projekt 1: Hangman

Spelet börjar att välja ett val från menun. Med första valet spelet börjar. Spelet visar med "_" hur många bokstaver i ordet. Genom gissa bokstaver det visar om den är rätt, fel eller redan skrivit. Fel gissning längden är ett minus än ordet. 

Spelet sparar också resultaten av spelaren till en txt fil av sista 5 genom att välja "2" andra val på menun.

Spelet har delat 3 filar. Hangman_game.py innehåller bara spelet i sig. save_file.py skapar sista 5 resultat och main.py är innehåller menu och huvudprogrammet.

Och spelet slutas genom att välja tredje valet.


![menu](/week3-lab/img/1.jpg "menu")
![menu](/week3-lab/img/2.jpg "menu")
![menu](/week3-lab/img/3.jpg "menu")
![menu](/week3-lab/img/4.jpg "menu")
![menu](/week3-lab/img/5.jpg "menu")
![menu](/week3-lab/img/6.jpg "menu")


### ---- inlämningens detaljer -----
### Skapa en version av det klassiska spelet Hangman.

- Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.

- Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.

- Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.

- Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.

### Krav på projekt
- Lösningen ska innehålla minst en klass med lämpliga metoder och attribut
- Lösningen ska innehålla minst en funktion (utöver klass-metoderna). Kan räcka med en main()-funktion
- Det ska gå att köra programmet
- Programmet ska fungera korrekt
