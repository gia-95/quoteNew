"""
- Una misura di affidabilità è sicuramente quanto si assomigliano le distribuzioni degli anni, 
  diciamo come indice di costanza negli ace
- Un'altra misura di affidabilità è guardare il numero di ace fatti dal giocatore (GS o no) (superfice) e 
  confrontarlo con gli ace subito dall'avversario.
  Es. se il giocatore fa di media 12 ace e l'avversario ne prende di media meno (es. 8), indicativamente 
  sarà più probabile l'under
"""

import matplotlib.pyplot as plt
import utils
import pandas as pd
import numpy as np
from scipy.stats import norm, poisson

#####   Parametri   ######  
GIOCATORE = "Karen Khachanov"
avversario = "Kamil Majchrzak"
SUPERFICE = "Grass"
TOURNAMENT = "Wimbledon"
UNDER_OVER_TYPE = "Under"
UNDER_OVER_VALUE = 18.5 

# Load CSV
df_match_2024 = pd.read_csv('data/atp_matches_2024.csv')
df_match_2023 = pd.read_csv('data/atp_matches_2023.csv')
df_match_2022 = pd.read_csv('data/atp_matches_2022.csv')

# Dataframes Ace (anno) - Corretto anche il typo nel nome della variabile
df_aces_2024 = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=False)
df_aces_2024_gSlam = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=True)
df_aces_2024_surface = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=False)
df_aces_2024_surface_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=True)


def plot_poisson_distributions(datasets_tuples, threshold_value, under_over_type):
    """
    Plotta le distribuzioni di Poisson per multiple datasets nella stessa finestra.
    
    Parameters:
    -----------
    datasets_tuples : list of tuples
        Lista di tuple nel formato (dataset, titolo) dove dataset deve contenere 
        la colonna "aces_giocatore"
    threshold_value : float
        Valore di soglia per calcolare la probabilità
    under_over_type : str
        "Under" per P(X <= threshold) o "Over" per P(X > threshold)
    """
    
    # Calcola il numero di subplot necessari
    n_datasets = len(datasets_tuples)
    n_cols = min(2, n_datasets)  # Massimo 2 colonne per risparmiare spazio
    n_rows = (n_datasets + n_cols - 1) // n_cols  # Calcola righe necessarie
    
    # Crea la figura con dimensioni adattate
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 4*n_rows))
    
    # Se c'è solo un subplot, axes non è un array
    if n_datasets == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes.flatten()
    elif n_cols == 1:
        axes = axes.flatten()
    else:
        axes = axes.flatten()
    
    # Nascondi subplot extra se necessario
    for i in range(n_datasets, len(axes)):
        axes[i].set_visible(False)
    
    for i, (dataset, titolo) in enumerate(datasets_tuples):
        # Verifica che il dataset abbia la colonna necessaria
        if 'aces_giocatore' not in dataset.columns:
            print(f"Warning: Dataset '{titolo}' non contiene la colonna 'aces_giocatore'")
            continue
        
        # Estrai i dati degli ace
        aces_data = dataset['aces_giocatore'].dropna()
        
        if len(aces_data) == 0:
            print(f"Warning: Dataset '{titolo}' non contiene dati validi")
            continue
        
        # Calcola statistiche
        n_samples = len(aces_data)
        media = np.mean(aces_data)
        varianza = np.var(aces_data)
        dev_std = np.std(aces_data)
        lambda_param = media  # Per Poisson, lambda = media
        
        # Calcola probabilità
        if under_over_type.lower() == "under":
            probabilita = poisson.cdf(threshold_value, lambda_param)
            prob_text = f"P(X ≤ {threshold_value})"
        else:  # over
            probabilita = 1 - poisson.cdf(threshold_value, lambda_param)
            prob_text = f"P(X > {threshold_value})"
        
        # Crea range per il plot
        x_max = max(int(aces_data.max()), int(lambda_param + 4*np.sqrt(lambda_param)))
        x_range = np.arange(0, x_max + 1)
        
        # Calcola PMF (Probability Mass Function)
        pmf_values = poisson.pmf(x_range, lambda_param)
        
        x = np.arange(0, x_max)
        p = poisson.pmf(x, media)
        
        # Plot
        ax = axes[i]
        ax.plot(x, p, 'ko-', linewidth=2, markersize=6, label='Poisson')
        bars = ax.bar(x_range, pmf_values, alpha=0.7, color='skyblue', edgecolor='navy')
        
        # Evidenzia la zona della soglia
        if under_over_type.lower() == "under":
            # Colora in rosso le barre <= threshold
            for j, val in enumerate(x_range):
                if val <= threshold_value:
                    bars[j].set_color('lightcoral')
        else:
            # Colora in rosso le barre > threshold
            for j, val in enumerate(x_range):
                if val > threshold_value:
                    bars[j].set_color('lightcoral')
        
        # Aggiungi linea verticale per la soglia
        ax.axvline(x=threshold_value, color='red', linestyle='--', linewidth=2, alpha=0.8)
        
        # Titolo
        ax.set_title(titolo, fontsize=12, fontweight='bold')
        
        # Labels
        ax.set_xlabel('Numero di Ace')
        ax.set_ylabel('Probabilità')
        
        # Leggenda con tutte le informazioni richieste
        legend_text = [
            f"Campioni: {n_samples}",
            f"Media: {media:.2f}",
            f"Lambda: {lambda_param:.2f}",
            f"Dev Std: {dev_std:.2f}",
            f"Varianza: {varianza:.2f}",
            f"{ 'Under' if under_over_type.lower() == 'under' else 'Over'} : {threshold_value}",
            f"{prob_text}: {probabilita:.3f}"
        ]
        
        # Aggiungi la leggenda in posizione più compatta
        ax.text(0.02, 0.98, '\n'.join(legend_text), 
                transform=ax.transAxes, 
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
                fontsize=8)
        
        # Griglia per migliorare la leggibilità
        ax.grid(True, alpha=0.3)
    
    # Titolo generale
    fig.suptitle(f'{GIOCATORE} - Ace 2024 ({under_over_type} {threshold_value})', 
                 fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.show()

# Esempio di utilizzo della funzione:
# Prepara i dataset come array di tuple
datasets_per_analisi = [
    (df_aces_2024, "ACE 2024 - Tutti i match"),
    (df_aces_2024_gSlam, "ACE 2024 - Grandi Slam"),
    (df_aces_2024_surface, f"ACE 2024 - Superficie {SUPERFICE}"),
    (df_aces_2024_surface_gSlam, f"ACE 2024 - Grandi Slam su {SUPERFICE}")

]

# Chiama la funzione
plot_poisson_distributions(datasets_per_analisi, UNDER_OVER_VALUE, UNDER_OVER_TYPE)