# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:11:34 2023

@author: kilian
"""


########################################################################
############## Exercice 0 : fonctions cosine et euclidean ##############
########################################################################

import numpy as np

def cosine(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

def euclidean(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)




########################################################################
############## Exercice 1 : standardize array function
########################################################################

import numpy as np

def standardize_data(arr):
    mean_vals = np.mean(arr, axis=1, keepdims=True)
    std_vals = np.std(arr, axis=1, keepdims=True)
    standardized_arr = (arr - mean_vals) / std_vals
    return standardized_arr


# Example usage :
arr = np.array([[1.2, -0.3, 1.3],
            [1.2, 2.0, 0.3]])

normalized_arr = standardize_data(arr)
print(normalized_arr)




########################################################################
############## Exercice 2 : confusion matrix
########################################################################

def compute_recall(m):
    recall = m.true_positive / (m.true_positive + m.false_negative)
    return recall

def compute_precision(m):
    precision = m.true_positive / (m.true_positive + m.false_positive)
    return precision

def compute_specificity(m):
    specificity = m.true_negative / (m.true_negative + m.false_positive)
    return specificity

def compute_accuracy(m):
    accuracy = (m.true_positive + m.true_negative) / (m.true_positive + m.true_negative + m.false_positive + m.false_negative)
    return accuracy



########################################################################
############## Exercice 3 : AvgSpend
########################################################################

# 'orders_df' est un dataframe avec deux colonnes : CustomerName et Order. Chaque ligne représente une colonne particulière d'un client.

# 'items_df' est un autre dataframe avec deux colonnes : ItemName et Price. Chaque ligne représente le prix d'un article en particulier.

# La fonction à écrire doit retourner un dataframe de deux colonnes CustomerName et AvgSpend et doit donc calculer pour chaque CustomerName,
# le montant moyen que ce client a dépensé sur ses commandes.

# La sortie doit être triée par CustomerName dans l'ordre alphabétique


import pandas as pd

def calculate_avg_spend(orders_df, items_df):
    # Fusionner les dataframes sur la colonne 'Order' dans orders_df et 'ItemName' dans items_df
    merged_df = pd.merge(orders_df, items_df, left_on='Order', right_on='ItemName')

    # Calculer la somme des dépenses par client
    total_spend_by_customer = merged_df.groupby('CustomerName')['Price'].sum()

    # Calculer le nombre de commandes par client
    order_count_by_customer = merged_df.groupby('CustomerName')['Order'].nunique()

    # Calculer le montant moyen dépensé par commande pour chaque client
    avg_spend_by_customer = total_spend_by_customer / order_count_by_customer

    # Créer le dataframe de sortie
    result_df = pd.DataFrame({'CustomerName': avg_spend_by_customer.index, 'AvgSpend': avg_spend_by_customer.values})

    # Trier le dataframe par 'CustomerName' dans l'ordre alphabétique
    result_df = result_df.sort_values(by='CustomerName')

    return result_df



# Exemple d'utilisation
orders_df = pd.DataFrame({'CustomerName': ['Alice', 'Bob', 'Alice', 'Bob'],
                          'Order': ['A1', 'B1', 'A2', 'B2']})

items_df = pd.DataFrame({'ItemName': ['A1', 'B1', 'A2', 'B2'],
                         'Price': [10, 20, 15, 25]})

result = calculate_avg_spend(orders_df, items_df)
print(result)





########################################################################
############## Exercice 4 : Machine's rank
########################################################################

# 'scores_df' un dataframe avec deux colonnes : BrandName et Score.
# Chaque ligne représente une marque de lave-linge et la note d'évaluation d'un lave-linge de cette marque par le client.
# A noter que certaines colonnes score peuvent contenir des valeurs Nan.

# 'prices_df' un dataframe avec deux colonnes : BrandName et Price. Chaque ligne représente le prix d'une marque particulière.

# Le dataframe de sortie doit avoir une seule valeur unique pour chaque BrandName et lui associer une colonne AvgScore qui sera le score moyen associé à cette marque.
# Le dataframe doit être trié par prix ajusté pour chaque marque dans l'ordre croissant.
# Le prix ajusté est défini comme étant le prix réel (Price) divisé par son score moyen (AvgScore).

# Dernière contrainte : l'ordre des indices doit être maintenu (première ligne avec indice 0 etc)


import pandas as pd

def rank_washing_machines(scores_df, prices_df):
    # Calculer la moyenne des scores par marque
    avg_scores = scores_df.groupby('BrandName')['Score'].mean()

    # Fusionner les dataframes scores_df et prices_df sur la colonne 'BrandName'
    merged_df = pd.merge(prices_df, avg_scores, left_on='BrandName', right_index=True)

    # Calculer la colonne 'AvgScore' et trier par 'Price' ajusté
    merged_df['AvgScore'] = merged_df['Score']
    merged_df['AdjustedPrice'] = merged_df['Price'] / merged_df['AvgScore']
    result_df = merged_df[['BrandName', 'Price', 'AvgScore', 'AdjustedPrice']].sort_values(by='AdjustedPrice')
    
    # Supprimer la colonne 'AdjustedPrice'
    result_df = result_df.drop(columns=['AdjustedPrice'])
    
    return result_df



# Exemple d'utilisation
scores_df = pd.DataFrame({'BrandName': ['BrandA', 'BrandB', 'BrandA', 'BrandB'],
                          'Score': [4.0, 3.5, 4.5, 3.0]})

prices_df = pd.DataFrame({'BrandName': ['BrandA', 'BrandB'],
                          'Price': [500, 600]})

result = rank_washing_machines(scores_df, prices_df)
print(result)










