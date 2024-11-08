import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance

# Läs in originaldata
url = "./carexp.csv"
df = pd.read_csv(url)

# Grundläggande dataanalys
print("Dataset Information:")
print("-" * 50)
print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nNull Values:")
print(df.isnull().sum())

# Analysera populäraste bilmärkena
plt.figure(figsize=(15, 6))
df['Car_Name'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Most Popular Car Models')
plt.xlabel('Car Model')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analysera bränsletyper
plt.figure(figsize=(10, 6))
df['Fuel_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Fuel Types')
plt.axis('equal')
plt.show()

# Analysera årsmodeller
plt.figure(figsize=(15, 6))
sns.histplot(data=df, x='Year', bins=20)
plt.title('Distribution of Car Models by Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Box plot för kilometer körda per bränsletyp
plt.figure(figsize=(12, 6))
sns.boxplot(x='Fuel_Type', y='Kms_Driven', data=df)
plt.title('Kilometers Driven by Fuel Type')
plt.xticks(rotation=45)
plt.show()

# Analysera genomsnittligt pris per bränsletyp
plt.figure(figsize=(12, 6))
df.groupby('Fuel_Type')['Selling_Price'].mean().plot(kind='bar')
plt.title('Average Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

# Konvertera kategoriska variabler till numeriska
le = LabelEncoder()
df_encoded = df.copy()
categorical_columns = ['Car_Name', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner']
for col in categorical_columns:
    df_encoded[col] = le.fit_transform(df_encoded[col])

# Visa korrelationsmatris
plt.figure(figsize=(12, 8))
sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Skriv ut sammanfattande statistik
print("\nSummary Statistics:")
print("-" * 50)
print(df.describe())

# Detaljerad analys av kategoriska variabler
print("\nCategory Distributions:")
print("-" * 50)
for col in categorical_columns:
    print(f"\n{col.upper()} Distribution:")
    print(df[col].value_counts())
    print(f"Unique values: {df[col].nunique()}")

# Kontrollera extremvärden
print("\nExtreme Values Analysis:")
print("-" * 50)
numerical_columns = ['Year', 'Selling_Price', 'Kms_Driven']
for col in numerical_columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col]
    print(f"\nOutliers in {col}:")
    print(f"Number of outliers: {len(outliers)}")
    print(f"Percentage of outliers: {(len(outliers)/len(df))*100:.2f}%")
    print(f"Range: {df[col].min()} to {df[col].max()}")

# Split the data into features and target variables
X = df_encoded.drop(['Fuel_Type', 'Selling_Price'], axis=1)
y_classification = df_encoded['Fuel_Type']
y_regression = df_encoded['Selling_Price']

# Split the data into training and testing sets
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(X, y_classification, test_size=0.2, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_regression, test_size=0.2, random_state=42)

# Classification model - RandomForest for fuel type prediction
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_clf, y_train_clf)
y_pred_clf = clf.predict(X_test_clf)
print("Classification Report for Fuel Type Prediction:")
print(classification_report(y_test_clf, y_pred_clf))

# Regression model - RandomForest for price prediction
reg = RandomForestRegressor(random_state=42)
reg.fit(X_train_reg, y_train_reg)
y_pred_reg = reg.predict(X_test_reg)
print("Mean Squared Error for Price Prediction:", mean_squared_error(y_test_reg, y_pred_reg))
print("R2 Score for Price Prediction:", r2_score(y_test_reg, y_pred_reg))

# Hyperparameter optimization with GridSearchCV
# Classification GridSearch
param_grid_clf = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5]
}
grid_search_clf = GridSearchCV(clf, param_grid_clf, cv=5, scoring='accuracy')
grid_search_clf.fit(X_train_clf, y_train_clf)
print("Best parameters for classification model:", grid_search_clf.best_params_)
print("Best classification accuracy:", grid_search_clf.best_score_)

# Regression GridSearch
param_grid_reg = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5]
}
grid_search_reg = GridSearchCV(reg, param_grid_reg, cv=5, scoring='r2')
grid_search_reg.fit(X_train_reg, y_train_reg)
print("Best parameters for regression model:", grid_search_reg.best_params_)
print("Best R2 score for regression:", grid_search_reg.best_score_)

# Feature Importance Analysis
# Classification Model Feature Importance
perm_importance_clf = permutation_importance(clf, X_test_clf, y_test_clf, n_repeats=10, random_state=42)
feature_names = X.columns
sorted_idx = perm_importance_clf.importances_mean.argsort()
plt.barh(feature_names[sorted_idx], perm_importance_clf.importances_mean[sorted_idx])
plt.xlabel("Permutation Importance")
plt.title("Feature Importance - Classification Model")
plt.show()

# Regression Model Feature Importance
perm_importance_reg = permutation_importance(reg, X_test_reg, y_test_reg, n_repeats=10, random_state=42)
sorted_idx = perm_importance_reg.importances_mean.argsort()
plt.barh(feature_names[sorted_idx], perm_importance_reg.importances_mean[sorted_idx])
plt.xlabel("Permutation Importance")
plt.title("Feature Importance - Regression Model")
plt.show()