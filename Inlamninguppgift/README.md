# Car Evaluation System

## Projektbeskrivning
Detta projekt är ett maskininlärningsbaserat system för att förutsäga bränsletyp och pris för bilar baserat på olika egenskaper. Målet är att bygga en applikation som använder tekniker för förbehandling av data, korsvalidering och hyperparameteroptimering för att förbättra modellens prestanda. Genom projektet är målet att lära sig hur man arbetar med maskininlärning inom fordonsklassificering och prissättning.

## Data och Funktioner
Projektet använder data som hämtas från en extern källfil (CSV) och har följande variabler:

- **Car_Name**: Bilmodellens namn.
- **Fuel_Type**: Bränsletyp (t.ex. bensin, diesel).
- **Seller_Type**: Om säljaren är en återförsäljare eller privatperson.
- **Transmission**: Typ av växellåda (manuell eller automatisk).
- **Owner**: Antal tidigare ägare.

### Målvariabler
1. **Klassificering av bränsletyp**: Förutspår bränsletypen med en klassificeringsmodell.
2. **Prisförutsägelse**: Förutspår bilens pris med en regressionsmodell.

## Modeller och Tekniker
- **Klassificering**: Använder `RandomForestClassifier` för att förutsäga bränsletyp.
- **Regression**: Använder `RandomForestRegressor` för prisförutsägelse.

## Databehandling och Förbehandling
- **Label-encoding**: Kategoriska variabler omvandlas till numeriska värden.
- **Normalisering och skalning**: Användning av `StandardScaler` för att skala data.

### Grid Search och Hyperparameteroptimering
Hyperparameteroptimering utförs med `GridSearchCV` för att förbättra modellens prestanda och hitta bästa parametrarna.

### Feature Importance
Genom att analysera och visualisera de viktigaste variablerna ökar modellens tolkbarhet.

## Begränsningar
Modellens prestanda kan vara begränsad av datakvalitet och tillgängliga funktioner.

## Kravspecifikation
### Datakrav
Projektet kräver både kategoriska och numeriska funktioner som beskrivs ovan.

### Programvarukrav
Bibliotek som används:
- **pandas**: Datahantering.
- **numpy**: Numeriska beräkningar.
- **scikit-learn**: Maskininlärningsmodeller och korsvalidering.
- **matplotlib och seaborn**: Datavisualisering.

## Klasser och Metoder
1. **DataPreprocessing**
   - `preprocess_data(df)`: Förbereder och label-encodar kategoriska variabler.
2. **GridSearch**
   - `perform_grid_search(X, y, is_regression)`: Utför hyperparameteroptimering med grid search och visualiserar viktiga parametrar.
3. **FeatureImportance**
   - `analyze_feature_importance(model, feature_names)`: Analyserar och visualiserar funktionernas betydelse i den tränade modellen.

## Användningsflöde
1. **Ladda Data**: Hämta data från en extern CSV-fil.
2. **Förbered Data**: Rensa och koda kategoriska data.
3. **Träna Modeller**: Använd random forest för klassificering och regression.
4. **Utvärdera Modeller**: Bedöm modellens prestanda med korsvalidering.
5. **Optimera Modeller**: Utför grid search för att finjustera hyperparametrar.
6. **Analysera Viktiga Funktioner**: Visualisera och tolka nyckelfunktioner som påverkar förutsägelserna.
