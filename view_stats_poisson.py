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
GENDER = "M"   
GIOCATORE = "Taylor Fritz"
avversario = "Taylor Fritz"
SUPERFICE = "Grass"
TOURNAMENT = "Wimbledon"
UNDER_OVER_TYPE = "Under"
UNDER_OVER_VALUE = 15.5 

# Load CSV
df_match_2024 = pd.read_csv(f"data/{'atp' if GENDER == 'M' else 'wta'}_matches_2024.csv")
df_match_2023 = pd.read_csv(f"data/{'atp' if GENDER == 'M' else 'wta'}_matches_2023.csv")
df_match_2022 = pd.read_csv(f"data/{'atp' if GENDER == 'M' else 'wta'}_matches_2022.csv")

# Dataframes Ace (anno) 
###  2024   ###
df_aces_2024 = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=False)
df_aces_2024_gSlam = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=True)
df_aces_2024_surface = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=False)
df_aces_2024_surface_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=True)
###  2023   ###
df_aces_2023 = utils.df_ace(GIOCATORE, df_match_2023, grandSlam=False)
df_aces_2023_gSlam = utils.df_ace(GIOCATORE, df_match_2023, grandSlam=True)
df_aces_2023_surface = utils.df_ace_surface(GIOCATORE, df_match_2023, SUPERFICE, grandSlam=False)
df_aces_2023_surface_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2023, SUPERFICE, grandSlam=True)
###  2022   ###
df_aces_2022 = utils.df_ace(GIOCATORE, df_match_2022, grandSlam=False)
df_aces_2022_gSlam = utils.df_ace(GIOCATORE, df_match_2022, grandSlam=True)
df_aces_2022_surface = utils.df_ace_surface(GIOCATORE, df_match_2022, SUPERFICE, grandSlam=False)
df_aces_2022_surface_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2022, SUPERFICE, grandSlam=True)

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
    
    # Colori migliorati per leggibilità: blu, arancione, verde
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 2024, 2023, 2022
    anni = [2024, 2023, 2022]

    for i, (dataset_per_anno, titolo) in enumerate(datasets_tuples):
        ax = axes[i]
        legend_lines = []
        legend_labels = []
        legend_texts = []

        for idx, datset_anno in enumerate(dataset_per_anno):
            # Verifica che il dataset abbia la colonna necessaria
            if 'aces_giocatore' not in datset_anno.columns:
                print(f"Warning: Dataset '{titolo}' non contiene la colonna 'aces_giocatore'")
                continue

            # Estrai i dati degli ace
            aces_data = datset_anno['aces_giocatore'].dropna()

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

            # Istogramma dei dati per ogni anno, con alpha decrescente e bordo evidenziato
            alphas_hist = [0.8, 0.4, 0.2]
            count, bins, ignored = ax.hist(
                aces_data,
                bins=range(int(aces_data.min()), int(aces_data.max()) + 2),
                density=True,
                alpha=alphas_hist[idx],
                color=colors[idx],
                edgecolor=colors[idx],        # bordo con lo stesso colore della distribuzione
                linewidth=2,                  # bordo ancora più spesso per evidenziare
                label=f'Dati {anni[idx]}',
                align='left'
            )

            # Distribuzione di Poisson
            alphas_curve = [1, 0.4, 0.2]
            x_max = int(aces_data.max()) + 2
            x = np.arange(0, x_max)
            p = poisson.pmf(x, media)
            line, = ax.plot(
                x, p, color=colors[idx], linewidth=2.5, markersize=6, marker='o',
                label=f'Poisson {anni[idx]}', alpha=alphas_curve[idx]
            )
            legend_lines.append(line)
            legend_labels.append(f'Poisson {anni[idx]}')

            # Box testo con statistiche per ogni anno
            legend_texts.append(
                f"{anni[idx]}:\n"
                f"  Campioni: {n_samples}\n"
                f"  Media: {media:.2f}\n"
                f"  Dev Std: {dev_std:.2f}\n"
                f"  Varianza: {varianza:.2f}\n"
                f"  { 'Under' if under_over_type.lower() == 'under' else 'Over'} : {threshold_value}\n"
                f"  {prob_text}: {probabilita:.3f}"
            )

        # Aggiungi linea verticale per la soglia
        ax.axvline(x=threshold_value, color='red', linestyle='--', linewidth=2, alpha=0.8)

        # Titolo
        ax.set_title(titolo, fontsize=12, fontweight='bold')

        # Labels
        ax.set_xlabel('Numero di Ace')
        ax.set_ylabel('Probabilità')

        # Box con statistiche di tutti gli anni
        ax.text(
            0.02, 0.98, '\n\n'.join(legend_texts),
            transform=ax.transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8),
            fontsize=8
        )

        # Legenda per le curve di Poisson
        ax.legend(handles=legend_lines, labels=legend_labels, loc='upper right', fontsize=9)

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
    ([df_aces_2024,df_aces_2023, df_aces_2022], "Matches ATP"),
    ([df_aces_2024_gSlam, df_aces_2023_gSlam, df_aces_2022_gSlam], "Matches GRANDI SLAM"),
    ([df_aces_2024_surface, df_aces_2023_surface, df_aces_2022_surface], f"ATP - Superficie {SUPERFICE}"),
    ([df_aces_2024_surface_gSlam, df_aces_2023_surface_gSlam, df_aces_2022_surface_gSlam], f" GRANDI SLAM - {SUPERFICE}")

]

# Chiama la funzione
plot_poisson_distributions(datasets_per_analisi, UNDER_OVER_VALUE, UNDER_OVER_TYPE)