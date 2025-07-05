"""""
Una misura di affidabilità è sicuramente quanto si assomigliano le distribuzioni degli anni, 
diciamo come indice di costanza negli ace
"""

import matplotlib.pyplot as plt
import utils
import pandas as pd
import numpy as np
from scipy.stats import norm, poisson

#####   Parametri   ######  
GIOCATORE = "Taylor Fritz"
avversario = "Jordan Thompson"
SUPERFICE = "Grass"
TOURNAMENT = "Wimbledon"
UNDER_OVER_TYPE = "Under"
UNDER_OVER_VALUE = 12.5  # Corretto: ora è un numero intero invece di una stringa


# Load CSV
df_match_2024 = pd.read_csv('data/atp_matches_2024.csv')
df_match_2023 = pd.read_csv('data/atp_matches_2023.csv')
df_match_2022 = pd.read_csv('data/atp_matches_2022.csv')


# Dataframes Ace (anno) - Corretto anche il typo nel nome della variabile
df_aces_2024 = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=False)
df_aces_2024_gSlam = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=True)
df_aces_2024_surface = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=False)
# df_aces_2024_surface = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=False)



def plot_aces_poisson(df, plot_title, threshold, giocatore, avversario, superficie, tournament, under_over_type, under_over_value):
    """
    Plotta la distribuzione dei valori 'aces_giocatore' e la sua distribuzione di Poisson.
    Calcola e mostra la probabilità di avere un valore minore di una soglia (threshold).
    Il threshold è passato come parametro.
    """
    data = df['aces_giocatore'].dropna()
    mu = data.mean()  # Per Poisson, lambda = media
    n = len(data)

    # Probabilità di avere un valore minore della soglia (P(X < threshold))
    prob = poisson.cdf(threshold - 1, mu)  # threshold - 1 perché cdf dà P(X <= k)

    # Istogramma dei dati
    plt.figure(figsize=(10, 6))
    count, bins, ignored = plt.hist(
        data,
        bins=range(int(data.min()), int(data.max()) + 2),
        density=True,
        alpha=0.6,
        color='g',
        label='Dati',
        align='left'
    )

    # Distribuzione di Poisson
    x_max = int(data.max()) + 2
    x = np.arange(0, x_max)
    p = poisson.pmf(x, mu)
    plt.plot(x, p, 'ko-', linewidth=2, markersize=6, label='Poisson')

    # Area sotto la curva fino alla soglia
    x_fill = np.arange(0, threshold)
    p_fill = poisson.pmf(x_fill, mu)
    plt.bar(
        x_fill,
        p_fill,
        color='skyblue',
        alpha=0.5,
        label=None  # Rimuovi la label per evitare doppia legenda
    )

    # Legenda separata per la probabilità target
    plt.axvline(threshold - 0.5, color='red', linestyle='--', label=None)
    plt.xlabel('Ace giocatore')
    plt.ylabel('Probabilità')
    # plt.title(f'Distribuzione Poisson degli Ace - {giocatore} vs {avversario}\n{tournament} ({superficie}) - Lambda={mu:.2f}, N={n}')
    plt.title(f' Distribuzione Poisson degli Ace di {giocatore} - {plot_title} - Lambda={mu:.2f}, N={n}')
    plt.xticks(range(int(data.min()), int(data.max()) + 1))
    plt.grid(True, alpha=0.3)

    # Aggiungi testo sulla figura
    info_text = (
        f"N: {n}\nLambda: {mu:.2f}\nVarianza: {mu:.2f}\n\n"
        f"Target: {under_over_type} {under_over_value}\nProbabilità: {prob:.3f}"
    )
    plt.text(
        0.99, 0.86, info_text,
        ha='right', va='top', transform=plt.gca().transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8)
    )

    # Crea due legende distinte
    handles, labels = plt.gca().get_legend_handles_labels()
    legend1 = plt.legend(handles, labels, loc='upper left')
    plt.gca().add_artist(legend1)
    # Legenda per la probabilità target
    plt.legend(
        [plt.Rectangle((0,0),1,1, color='skyblue', alpha=0.5),
         plt.Line2D([0], [0], color='red', linestyle='--')],
        [f'P(X < {threshold}) = {prob:.3f}', f'Target: {under_over_type} {under_over_value}'],
        loc='upper right'
    )

    plt.show()

# def plot_aces_gaussian(df, threshold, giocatore, avversario, superficie, tournament, under_over_type, under_over_value):
    """
    Plotta la distribuzione dei valori 'aces_giocatore' e la sua gaussiana.
    Calcola e mostra la probabilità di avere un valore minore di una soglia (threshold).
    Il threshold è passato come parametro.
    """
    data = df['aces_giocatore'].dropna()
    mu, std = data.mean(), data.std()

    # Probabilità di avere un valore minore della soglia
    prob = norm.cdf(threshold, mu, std)

    # Istogramma dei dati
    plt.figure(figsize=(10, 6))
    count, bins, ignored = plt.hist(data, bins=10, density=True, alpha=0.6, color='g', label='Dati')

    # Curva gaussiana
    xmin, xmax = bins[0], bins[-1]
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label='Gaussiana')

    # Area sotto la curva fino alla soglia
    x_fill = np.linspace(xmin, threshold, 100)
    p_fill = norm.pdf(x_fill, mu, std)
    plt.fill_between(x_fill, p_fill, color='skyblue', alpha=0.5, label=f'P(X < {threshold}) = {prob:.2f}')

    plt.axvline(threshold, color='red', linestyle='--', label=f'Threshold = {threshold}')
    plt.xlabel('Ace giocatore')
    plt.ylabel('Densità')
    plt.title(f'Distribuzione e Gaussiana degli Ace per Match\nMedia: {mu:.2f}, Std: {std:.2f}')
    plt.legend()
    plt.show()


# Chiamata delle funzioni con tutti i parametri
# plot_aces_gaussian(df_aces_2024, UNDER_OVER_VALUE, GIOCATORE, avversario, SUPERFICE, TOURNAMENT, UNDER_OVER_TYPE, UNDER_OVER_VALUE)
fig, axs = plt.subplots(1, 3, figsize=(20, 6))

dfs = [
    (df_aces_2024, "ATP"),
    (df_aces_2024_gSlam, "GRANDI SLAM"),
    (df_aces_2024_surface, f"ATP - surface:{SUPERFICE}")
]

for ax, (df, plot_title) in zip(axs, dfs):
    data = df['aces_giocatore'].dropna()
    mu = data.mean()
    n = len(data)
    prob = poisson.cdf(UNDER_OVER_VALUE - 1, mu)
    # Istogramma dei dati
    count, bins, ignored = ax.hist(
        data,
        bins=range(int(data.min()), int(data.max()) + 2),
        density=True,
        alpha=0.6,
        color='g',
        label='Dati',
        align='left'
    )
    # Distribuzione di Poisson
    x_max = int(data.max()) + 2
    x = np.arange(0, x_max)
    p = poisson.pmf(x, mu)
    ax.plot(x, p, 'ko-', linewidth=2, markersize=6, label='Poisson')
    # Area sotto la curva fino alla soglia
    x_fill = np.arange(0, UNDER_OVER_VALUE)
    p_fill = poisson.pmf(x_fill, mu)
    ax.bar(
        x_fill,
        p_fill,
        color='skyblue',
        alpha=0.5,
        label=None
    )
    ax.axvline(UNDER_OVER_VALUE - 0.5, color='red', linestyle='--', label=None)
    ax.set_xlabel('Ace giocatore')
    ax.set_ylabel('Probabilità')
    ax.set_title(f'{plot_title}\nLambda={mu:.2f}, N={n}')
    ax.set_xticks(range(int(data.min()), int(data.max()) + 1))
    ax.grid(True, alpha=0.3)
    info_text = (
        f"N: {n}\nLambda: {mu:.2f}\nVarianza: {mu:.2f}\n\n"
        f"Target: {UNDER_OVER_TYPE} {UNDER_OVER_VALUE}\nProbabilità: {prob:.3f}"
    )
    ax.text(
        0.99, 0.86, info_text,
        ha='right', va='top', transform=ax.transAxes, fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8)
    )
    handles, labels = ax.get_legend_handles_labels()
    legend1 = ax.legend(handles, labels, loc='upper left')
    ax.add_artist(legend1)
    ax.legend(
        [plt.Rectangle((0,0),1,1, color='skyblue', alpha=0.5),
         plt.Line2D([0], [0], color='red', linestyle='--')],
        [f'P(X < {UNDER_OVER_VALUE}) = {prob:.3f}', f'Target: {UNDER_OVER_TYPE} {UNDER_OVER_VALUE}'],
        loc='upper right'
    )

plt.tight_layout()
plt.show()