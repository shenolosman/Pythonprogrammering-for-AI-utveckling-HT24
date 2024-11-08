# Bilprediktion - Steg för steg

Sammanfattningsvis är det en supervised learning-ansats där jag har tränat både en klassificeringsmodell(RandomForestClassifier) och en regressionsmodell(RandomForestRegressor) för att förutsäga bränsletyp och bilpris.

colab länk: https://colab.research.google.com/drive/1Jk00_-2AZrMfbS8O75gn6UtHnzqMhe4Z#scrollTo=ifdMciJe2oXk

## Steg 1: Datainläsning
Man börjar med att ladda in den data som ska användas för analysen. Denna data innehåller information om olika bilar, såsom bilmodell, bränsletyp, pris och körsträcka.

## Steg 2: Datautforskning
När datan är inladdad undersöks den närmare. Man kollar antalet bilar, deras egenskaper och om det finns några problem med datan, till exempel saknade värden.

## Steg 3: Analys av populära bilmodeller
Man tittar på vilka bilmodeller som är mest populära. En graf skapas för att visa de tio mest förekommande modellerna.

## Steg 4: Analys av bränsletyper
Fördelningen av olika bränsletyper i datan undersöks. Ett cirkeldiagram används för att visualisera andelen bilar med varje bränsletyp.

## Steg 5: Analys av årsmodeller
Fördelningen av årsmodeller analyseras. Ett histogram används för att visa antalet bilar för varje årsmodell.

## Steg 6: Analys av körsträckor
Körsträckorna för olika bränsletyper jämförs. Ett boxplotdiagram används för att visualisera körsträckorna för varje bränsletyp.

## Steg 7: Analys av priser
Priserna för olika bränsletyper analyseras. Ett stapeldiagram används för att visa det genomsnittliga priset för varje bränsletyp.

## Steg 8: Förberedelse för maskininlärning
Datan förbereds för att kunna användas i maskininlärningsmodeller. Kategoriska variabler, som bilmodell och bränsletyp, omvandlas till numeriska värden.

## Steg 9: Träning av klassificeringsmodell
En slumpmässig skogsklassificerare (RandomForestClassifier) tränas för att förutsäga bränsletyp baserat på bilens övriga egenskaper.

## Steg 10: Träning av regressionsmodell
En slumpmässig skogsregressor (RandomForestRegressor) tränas för att förutsäga bilpriset baserat på bilens egenskaper.

## Steg 11: Optimering av modeller
Modellerna optimeras genom att justera deras hyperparametrar med hjälp av GridSearchCV.

## Steg 12: Analys av viktiga egenskaper
Man analyserar vilka egenskaper som är viktigast för klassificeringen och regressionen. Resultaten visualiseras i stapeldiagram.