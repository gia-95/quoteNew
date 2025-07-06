import warnings
import pandas as pd
import matplotlib.pyplot as plt
import utils
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
print()



#####   Parametri   ######  
GIOCATORE = "Karen Khachanov"
avversario = "Kamil Majchrzak"
SUPERFICE = "Grass"
TOURNAMENT = "Wimbledon"
UNDER_OVER_TYPE = "Under"
UNDER_OVER_VALUE = 18.5 



df_match_2024 = pd.read_csv('data/atp_matches_2024.csv')
df_match_2023 = pd.read_csv('data/atp_matches_2023.csv')
df_match_2022 = pd.read_csv('data/atp_matches_2022.csv')


######################################################
#                   2024                             #
######################################################
###------------  ATP ---------------------------------------
df_aces_2024 = utils.df_ace(GIOCATORE, df_match_2024)
n_matches_2024 = len(df_aces_2024)
mean_ace_2024 = df_aces_2024['aces_giocatore'].mean()
dev_std_2024_aces = df_aces_2024['aces_giocatore'].std()
# VS avversario
df_aces_2024_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2024)
n_matches_2024_vs_opp = len(df_aces_2024_vs_opp)
mean_ace_2024_vs_opp = df_aces_2024_vs_opp['aces_giocatore'].mean() if len(df_aces_2024_vs_opp) != 0  else 0
dev_std_aces_2024_vs_opp = df_aces_2024_vs_opp['aces_giocatore'].std() if len(df_aces_2024_vs_opp) != 0  else 0
# Superfice
df_aces_2024_superfice = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE)
n_matches_2024_superfice = len(df_aces_2024_superfice)
mean_ace_2024_superfice = df_aces_2024_superfice['aces_giocatore'].mean()
dev_std_aces_2024_superfice = df_aces_2024_superfice['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2024_superfice_vs_opp = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2024, SUPERFICE)
n_matches_2024_superfice_vs_opp = len(df_aces_2024_superfice_vs_opp)
mean_ace_2024_superfice_vs_opp = df_aces_2024_superfice_vs_opp['aces_giocatore'].mean()
dev_std_aces_2024_superfice_vs_opp = df_aces_2024_superfice_vs_opp['aces_giocatore'].std()
### * SUBITI AVVERSARIO
df_ace_subitiAvversario_2024 = utils.df_ace_subiti_avversario(avversario, df_match_2024, False)
n_matches_subitiAvversario_2024 = len(df_ace_subitiAvversario_2024)
mean_ace__subitiAvversario_2024 = df_ace_subitiAvversario_2024['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2024_aces = df_ace_subitiAvversario_2024['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE
df_ace_subitiAvversario_surface_2024 = utils.df_ace_subiti_avversario_surface(avversario, df_match_2024, SUPERFICE, False)
n_matches_subitiAvversario_surface_2024 = len(df_ace_subitiAvversario_surface_2024)
mean_ace__subitiAvversario_surface_2024 = df_ace_subitiAvversario_surface_2024['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2024_aces = df_ace_subitiAvversario_surface_2024['aces_giocatore'].std()


###------------  GRANDI SLAM ---------------------------------------
df_aces_2024_gSlam = utils.df_ace(GIOCATORE, df_match_2024, grandSlam=True)
n_matches_2024_gSlam = len(df_aces_2024_gSlam)
mean_ace_2024_gSlam = df_aces_2024_gSlam['aces_giocatore'].mean()
dev_std_aces_2024_gSlam = df_aces_2024_gSlam['aces_giocatore'].std()
# VS avversario
df_aces_2024_gSlam_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2024, grandSlam=True)
n_matches_2024_gSlam_vs_opp = len(df_aces_2024_gSlam_vs_opp)
mean_ace_2024_gSlam_vs_opp = df_aces_2024_gSlam_vs_opp['aces_giocatore'].mean() if len(df_aces_2024_gSlam_vs_opp) != 0  else 0
dev_std_aces_2024_gSlam_vs_opp = df_aces_2024_gSlam_vs_opp['aces_giocatore'].std() if len(df_aces_2024_gSlam_vs_opp) != 0  else 0
# Superfice
df_aces_2024_superfice_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2024, SUPERFICE, grandSlam=True)
n_matches_2024_superfice_gSlam = len(df_aces_2024_superfice_gSlam)
mean_ace_2024_superfice_gSlam = df_aces_2024_superfice_gSlam['aces_giocatore'].mean()
dev_std_aces_2024_superfice_gSlam = df_aces_2024_superfice_gSlam['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2024_superfice_vs_opp_gSlam = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2024, SUPERFICE, grandSlam=True)
n_matches_2024_superfice_vs_opp_gSlam = len(df_aces_2024_superfice_vs_opp_gSlam)
mean_ace_2024_superfice_vs_opp_gSlam = df_aces_2024_superfice_vs_opp_gSlam['aces_giocatore'].mean()
dev_std_aces_2024_superfice_vs_opp_gSlam = df_aces_2024_superfice_vs_opp_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO GS
df_ace_subitiAvversario_2024_gSlam = utils.df_ace_subiti_avversario(avversario, df_match_2024, True)
n_matches_subitiAvversario_2024_gSlam = len(df_ace_subitiAvversario_2024_gSlam)
mean_ace__subitiAvversario_2024_gSlam = df_ace_subitiAvversario_2024_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2024_aces_gSlam = df_ace_subitiAvversario_2024_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE GS
df_ace_subitiAvversario_surface_2024_gSlam = utils.df_ace_subiti_avversario_surface(avversario, df_match_2024, SUPERFICE, True)
n_matches_subitiAvversario_surface_2024_gSlam = len(df_ace_subitiAvversario_surface_2024_gSlam)
mean_ace__subitiAvversario_surface_2024_gSlam = df_ace_subitiAvversario_surface_2024_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2024_ace_gSlams = df_ace_subitiAvversario_surface_2024_gSlam['aces_giocatore'].std()


### TORNAMENT
df_aces_2024_tournament = utils.df_ace_tournament(GIOCATORE, df_match_2024,TOURNAMENT)
n_matches_2024_tournament = len(df_aces_2024_tournament)
mean_ace_2024_tournament = df_aces_2024_tournament['aces_giocatore'].mean()
dev_std_aces_2024_tournament = df_aces_2024_tournament['aces_giocatore'].std()
# TOURNAMENT VS avversario
df_aces_2024_tournament_vs_opp = utils.df_ace_tournament_vs_opponent(GIOCATORE, avversario, df_match_2024, TOURNAMENT)
n_matches_2024_tournament_vs_opp = len(df_aces_2024_tournament_vs_opp)
mean_ace_2024_tournament_vs_opp = df_aces_2024_tournament_vs_opp['aces_giocatore'].mean()
dev_std_aces_2024_tournament_vs_opp = df_aces_2024_tournament_vs_opp['aces_giocatore'].std()



######################################################
#                   2023                             #
######################################################

###------------  CIRCUITO ATP ---------------------------------------
df_aces_2023 = utils.df_ace(GIOCATORE, df_match_2023)
n_matches_2023 = len(df_aces_2023)
mean_ace_2023 = df_aces_2023['aces_giocatore'].mean()
dev_std_aces_2023 = df_aces_2023['aces_giocatore'].std()
# VS avversario
df_aces_2023_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2023)
n_matches_2023_vs_opp = len(df_aces_2023_vs_opp)
mean_ace_2023_vs_opp = df_aces_2023_vs_opp['aces_giocatore'].mean() if len(df_aces_2023_vs_opp) != 0  else 0
dev_std_aces_2023_vs_opp = df_aces_2023_vs_opp['aces_giocatore'].std() if len(df_aces_2023_vs_opp) != 0  else 0
# Superfice
df_aces_2023_superfice = utils.df_ace_surface(GIOCATORE, df_match_2023, SUPERFICE)
n_matches_2023_superfice = len(df_aces_2023_superfice)
mean_ace_2023_superfice = df_aces_2023_superfice['aces_giocatore'].mean()
dev_std_aces_2023_superfice = df_aces_2023_superfice['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2023_superfice_vs_opp = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2023, SUPERFICE)
n_matches_2023_superfice_vs_opp = len(df_aces_2023_superfice_vs_opp)
mean_ace_2023_superfice_vs_opp = df_aces_2023_superfice_vs_opp['aces_giocatore'].mean()
dev_std_aces_2023_superfice_vs_opp = df_aces_2023_superfice_vs_opp['aces_giocatore'].std()
### * SUBITI AVVERSARIO
df_ace_subitiAvversario_2023 = utils.df_ace_subiti_avversario(avversario, df_match_2023, False)
n_matches_subitiAvversario_2023 = len(df_ace_subitiAvversario_2023)
mean_ace__subitiAvversario_2023 = df_ace_subitiAvversario_2023['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2023_aces = df_ace_subitiAvversario_2023['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE
df_ace_subitiAvversario_surface_2023 = utils.df_ace_subiti_avversario_surface(avversario, df_match_2023, SUPERFICE, False)
n_matches_subitiAvversario_surface_2023 = len(df_ace_subitiAvversario_surface_2023)
mean_ace__subitiAvversario_surface_2023 = df_ace_subitiAvversario_surface_2023['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2023_aces = df_ace_subitiAvversario_surface_2023['aces_giocatore'].std()

###------------  GRANDI SLAM ---------------------------------------
df_aces_2023_gSlam = utils.df_ace(GIOCATORE, df_match_2023, grandSlam=True)
n_matches_2023_gSlam = len(df_aces_2023_gSlam)
mean_ace_2023_gSlam = df_aces_2023_gSlam['aces_giocatore'].mean()
dev_std_aces_2023_gSlam = df_aces_2023_gSlam['aces_giocatore'].std()
# VS avversario
df_aces_2023_gSlam_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2023, grandSlam=True)
n_matches_2023_gSlam_vs_opp = len(df_aces_2023_gSlam_vs_opp)
mean_ace_2023_gSlam_vs_opp = df_aces_2023_gSlam_vs_opp['aces_giocatore'].mean() if len(df_aces_2023_gSlam_vs_opp) != 0  else 0
dev_std_aces_2023_gSlam_vs_opp = df_aces_2023_gSlam_vs_opp['aces_giocatore'].std() if len(df_aces_2023_gSlam_vs_opp) != 0  else 0
# Superfice
df_aces_2023_superfice_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2023, SUPERFICE, grandSlam=True)
n_matches_2023_superfice_gSlam = len(df_aces_2023_superfice_gSlam)
mean_ace_2023_superfice_gSlam = df_aces_2023_superfice_gSlam['aces_giocatore'].mean()
dev_std_aces_2023_superfice_gSlam = df_aces_2023_superfice_gSlam['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2023_superfice_vs_opp_gSlam = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2023, SUPERFICE, grandSlam=True)
n_matches_2023_superfice_vs_opp_gSlam = len(df_aces_2023_superfice_vs_opp_gSlam)
mean_ace_2023_superfice_vs_opp_gSlam = df_aces_2023_superfice_vs_opp_gSlam['aces_giocatore'].mean()
dev_std_aces_2023_superfice_vs_opp_gSlam = df_aces_2023_superfice_vs_opp_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO GS
df_ace_subitiAvversario_2023_gSlam = utils.df_ace_subiti_avversario(avversario, df_match_2023, True)
n_matches_subitiAvversario_2023_gSlam = len(df_ace_subitiAvversario_2023_gSlam)
mean_ace__subitiAvversario_2023_gSlam = df_ace_subitiAvversario_2023_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2023_aces_gSlam = df_ace_subitiAvversario_2023_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE GS
df_ace_subitiAvversario_surface_2023_gSlam = utils.df_ace_subiti_avversario_surface(avversario, df_match_2023, SUPERFICE, True)
n_matches_subitiAvversario_surface_2023_gSlam = len(df_ace_subitiAvversario_surface_2023_gSlam)
mean_ace__subitiAvversario_surface_2023_gSlam = df_ace_subitiAvversario_surface_2023_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2023_ace_gSlams = df_ace_subitiAvversario_surface_2023_gSlam['aces_giocatore'].std()

### TORNAMENT
df_aces_2023_tournament = utils.df_ace_tournament(GIOCATORE, df_match_2023,TOURNAMENT)
n_matches_2023_tournament = len(df_aces_2023_tournament)
mean_ace_2023_tournament = df_aces_2023_tournament['aces_giocatore'].mean()
dev_std_aces_2023_tournament = df_aces_2023_tournament['aces_giocatore'].std()
# TOURNAMENT VS avversario
df_aces_2023_tournament_vs_opp = utils.df_ace_tournament_vs_opponent(GIOCATORE, avversario, df_match_2023, TOURNAMENT)
n_matches_2023_tournament_vs_opp = len(df_aces_2023_tournament_vs_opp)
mean_ace_2023_tournament_vs_opp = df_aces_2023_tournament_vs_opp['aces_giocatore'].mean()
dev_std_aces_2023_tournament_vs_opp = df_aces_2023_tournament_vs_opp['aces_giocatore'].std()

######################################################
#                   2022                             #
######################################################
###------------  ATP ---------------------------------------
df_aces_2022 = utils.df_ace(GIOCATORE, df_match_2022)
n_matches_2022 = len(df_aces_2022)
mean_ace_2022 = df_aces_2022['aces_giocatore'].mean()
dev_std_aces_2022 = df_aces_2022['aces_giocatore'].std()
# VS avversario
df_aces_2022_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2022)
n_matches_2022_vs_opp = len(df_aces_2022_vs_opp)
mean_ace_2022_vs_opp = df_aces_2022_vs_opp['aces_giocatore'].mean() if len(df_aces_2022_vs_opp) != 0  else 0
dev_std_aces_2022_vs_opp = df_aces_2022_vs_opp['aces_giocatore'].std() if len(df_aces_2022_vs_opp) != 0  else 0
# Superfice
df_aces_2022_superfice = utils.df_ace_surface(GIOCATORE, df_match_2022, SUPERFICE)
n_matches_2022_superfice = len(df_aces_2022_superfice)
mean_ace_2022_superfice = df_aces_2022_superfice['aces_giocatore'].mean()
dev_std_aces_2022_superfice = df_aces_2022_superfice['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2022_superfice_vs_opp = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2022, SUPERFICE)
n_matches_2022_superfice_vs_opp = len(df_aces_2022_superfice_vs_opp)
mean_ace_2022_superfice_vs_opp = df_aces_2022_superfice_vs_opp['aces_giocatore'].mean()
dev_std_aces_2022_superfice_vs_opp = df_aces_2022_superfice_vs_opp['aces_giocatore'].std()
### * SUBITI AVVERSARIO
df_ace_subitiAvversario_2022 = utils.df_ace_subiti_avversario(avversario, df_match_2022, False)
n_matches_subitiAvversario_2022 = len(df_ace_subitiAvversario_2022)
mean_ace__subitiAvversario_2022 = df_ace_subitiAvversario_2022['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2022_aces = df_ace_subitiAvversario_2022['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE
df_ace_subitiAvversario_surface_2022 = utils.df_ace_subiti_avversario_surface(avversario, df_match_2022, SUPERFICE, False)
n_matches_subitiAvversario_surface_2022 = len(df_ace_subitiAvversario_surface_2022)
mean_ace__subitiAvversario_surface_2022 = df_ace_subitiAvversario_surface_2022['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2022_aces = df_ace_subitiAvversario_surface_2022['aces_giocatore'].std()


###------------  GRANDI SLAM ---------------------------------------
df_aces_2022_gSlam = utils.df_ace(GIOCATORE, df_match_2022, grandSlam=True)
n_matches_2022_gSlam = len(df_aces_2022_gSlam)
mean_ace_2022_gSlam = df_aces_2022_gSlam['aces_giocatore'].mean()
dev_std_aces_2022_gSlam = df_aces_2022_gSlam['aces_giocatore'].std()
# VS avversario
df_aces_2022_gSlam_vs_opp = utils.df_ace_vs_opponent(GIOCATORE, avversario, df_match_2022, grandSlam=True)
n_matches_2022_gSlam_vs_opp = len(df_aces_2022_gSlam_vs_opp)
mean_ace_2022_gSlam_vs_opp = df_aces_2022_gSlam_vs_opp['aces_giocatore'].mean() if len(df_aces_2022_gSlam_vs_opp) != 0  else 0
dev_std_aces_2022_gSlam_vs_opp = df_aces_2022_gSlam_vs_opp['aces_giocatore'].std() if len(df_aces_2022_gSlam_vs_opp) != 0  else 0
# Superfice
df_aces_2022_superfice_gSlam = utils.df_ace_surface(GIOCATORE, df_match_2022, SUPERFICE, grandSlam=True)
n_matches_2022_superfice_gSlam = len(df_aces_2022_superfice_gSlam)
mean_ace_2022_superfice_gSlam = df_aces_2022_superfice_gSlam['aces_giocatore'].mean()
dev_std_aces_2022_superfice_gSlam = df_aces_2022_superfice_gSlam['aces_giocatore'].std()
# Superfice VS avversario
df_aces_2022_superfice_vs_opp_gSlam = utils.df_ace_superfice_vs_opponent(GIOCATORE, avversario, df_match_2022, SUPERFICE, grandSlam=True)
n_matches_2022_superfice_vs_opp_gSlam = len(df_aces_2022_superfice_vs_opp_gSlam)
mean_ace_2022_superfice_vs_opp_gSlam = df_aces_2022_superfice_vs_opp_gSlam['aces_giocatore'].mean()
dev_std_aces_2022_superfice_vs_opp_gSlam = df_aces_2022_superfice_vs_opp_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO GS
df_ace_subitiAvversario_2022_gSlam = utils.df_ace_subiti_avversario(avversario, df_match_2022, True)
n_matches_subitiAvversario_2022_gSlam = len(df_ace_subitiAvversario_2022_gSlam)
mean_ace__subitiAvversario_2022_gSlam = df_ace_subitiAvversario_2022_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_2022_aces_gSlam = df_ace_subitiAvversario_2022_gSlam['aces_giocatore'].std()
### * SUBITI AVVERSARIO SU SUPERFICE GS
df_ace_subitiAvversario_surface_2022_gSlam = utils.df_ace_subiti_avversario_surface(avversario, df_match_2022, SUPERFICE, True)
n_matches_subitiAvversario_surface_2022_gSlam = len(df_ace_subitiAvversario_surface_2022_gSlam)
mean_ace__subitiAvversario_surface_2022_gSlam = df_ace_subitiAvversario_surface_2022_gSlam['aces_giocatore'].mean()
dev_std_ace_ubitiAvversario_surface_2022_ace_gSlams = df_ace_subitiAvversario_surface_2022_gSlam['aces_giocatore'].std()


### TORNAMENT
df_aces_2022_tournament = utils.df_ace_tournament(GIOCATORE, df_match_2022,TOURNAMENT)
n_matches_2022_tournament = len(df_aces_2022_tournament)
mean_ace_2022_tournament = df_aces_2022_tournament['aces_giocatore'].mean()
dev_std_aces_2022_tournament = df_aces_2022_tournament['aces_giocatore'].std()
# TOURNAMENT VS avversario
df_aces_2022_tournament_vs_opp = utils.df_ace_tournament_vs_opponent(GIOCATORE, avversario, df_match_2022, TOURNAMENT)
n_matches_2022_tournament_vs_opp = len(df_aces_2022_tournament_vs_opp)
mean_ace_2022_tournament_vs_opp = df_aces_2022_tournament_vs_opp['aces_giocatore'].mean()
dev_std_aces_2022_tournament_vs_opp = df_aces_2022_tournament_vs_opp['aces_giocatore'].std()




print(f"\n###############################################################")
print(f"# GIOCATORE:   {GIOCATORE} {' ' * (45 - len(GIOCATORE))} #")
print(f"# AVVERSARIO:  {avversario} {' ' * (45 - len(avversario))} #")
print(f"# SUPERFICE:   {SUPERFICE} {' ' * (45 - len(SUPERFICE))} #")
print(f"###############################################################")

print(f"\n###############################################################")
print(f"#########################   2024    ###########################")
print(f"###############################################################")# Tutte le partite
print("\n---------------------  ATP  ---------------------")
print(f"  Partite giocate: {n_matches_2024}")
print(f"  Aces : {mean_ace_2024:.2f} | std: {dev_std_2024_aces:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite giocate su {SUPERFICE}: {n_matches_2024_superfice}")
print(f"  Aces su {SUPERFICE}: {mean_ace_2024_superfice:.2f} | std: {dev_std_aces_2024_superfice:.2f}")
# VS Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2024_vs_opp}")
print(f"  Aces VS {avversario}: {mean_ace_2024_vs_opp:.2f} | std: {dev_std_aces_2024_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2024_superfice_vs_opp}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2024_superfice_vs_opp:.2f} | std: {dev_std_aces_2024_superfice_vs_opp:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2024}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2024:.2f} | std: {dev_std_ace_ubitiAvversario_2024_aces:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2024}): {mean_ace__subitiAvversario_surface_2024:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2024_aces:.2f}")


### GRANDI SLAM
print("\n\n--------------  GRANDI SLAM  --------------")
print(f"  Partite giocate: {n_matches_2024_gSlam}")
print(f"  Media aces : {mean_ace_2024_gSlam:.2f} | std: {dev_std_aces_2024_gSlam:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite GS giocate su {SUPERFICE}: {n_matches_2024_superfice_gSlam}")
print(f"  Media aces su {SUPERFICE}: {mean_ace_2024_superfice_gSlam:.2f} | std: {dev_std_aces_2024_superfice_gSlam:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2024_gSlam_vs_opp}")
print(f"  Media aces VS {avversario}: {mean_ace_2024_gSlam_vs_opp:.2f} | std: {dev_std_aces_2024_gSlam_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2024_superfice_vs_opp_gSlam}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2024_superfice_vs_opp_gSlam:.2f} | std: {dev_std_aces_2024_superfice_vs_opp_gSlam:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2024_gSlam}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2024_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_2024_aces_gSlam:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2024_gSlam}): {mean_ace__subitiAvversario_surface_2024_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2024_aces:.2f}")

### TOURNAMENT
print(f"\n\n--------------  TOURNAMENT: {TOURNAMENT}  (2024)  --------------")
print(f"  Partite giocate: {n_matches_2024_tournament}")
print(f"  Media aces : {mean_ace_2024_tournament:.2f} | std: {dev_std_aces_2024_tournament:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite giocate VS {avversario} in {TOURNAMENT}: {n_matches_2024_tournament_vs_opp}")
print(f"  Media aces VS {avversario} in {TOURNAMENT}: {mean_ace_2024_tournament_vs_opp:.2f} | std: {dev_std_aces_2024_tournament_vs_opp:.2f}")



print(f"\n###############################################################")
print(f"#########################   2023    ###########################")
print(f"###############################################################")# Tutte le partite
print("\n---------------------  ATP  ---------------------")
print(f"  Partite giocate: {n_matches_2023}")
print(f"  Aces : {mean_ace_2023:.2f} | std: {dev_std_aces_2023:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite giocate su {SUPERFICE}: {n_matches_2023_superfice}")
print(f"  Aces su {SUPERFICE}: {mean_ace_2023_superfice:.2f} | std: {dev_std_aces_2023_superfice:.2f}")
# VS Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2023_vs_opp}")
print(f"  Aces VS {avversario}: {mean_ace_2023_vs_opp:.2f} | std: {dev_std_aces_2023_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2023_superfice_vs_opp}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2023_superfice_vs_opp:.2f} | std: {dev_std_aces_2023_superfice_vs_opp:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2023}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2023:.2f} | std: {dev_std_ace_ubitiAvversario_2023_aces:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2023}): {mean_ace__subitiAvversario_surface_2023:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2023_aces:.2f}")


# Grandi Slam
print("\n\n--------------  GRANDI SLAM  --------------")
print(f"  Partite giocate: {n_matches_2023_gSlam}")
print(f"  Media aces : {mean_ace_2023_gSlam:.2f} | std: {dev_std_aces_2023_gSlam:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite GS giocate su {SUPERFICE}: {n_matches_2023_superfice_gSlam}")
print(f"  Media aces su {SUPERFICE}: {mean_ace_2023_superfice_gSlam:.2f} | std: {dev_std_aces_2023_superfice_gSlam:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2023_gSlam_vs_opp}")
print(f"  Media aces VS {avversario}: {mean_ace_2023_gSlam_vs_opp:.2f} | std: {dev_std_aces_2023_gSlam_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2023_superfice_vs_opp_gSlam}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2023_superfice_vs_opp_gSlam:.2f} | std: {dev_std_aces_2023_superfice_vs_opp_gSlam:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2023_gSlam}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2023_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_2023_aces_gSlam:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2023_gSlam}): {mean_ace__subitiAvversario_surface_2023_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2023_aces:.2f}")

# Tournament
print(f"\n\n--------------  TOURNAMENT: {TOURNAMENT}  (2023)  --------------")
print(f"  Partite giocate: {n_matches_2023_tournament}")
print(f"  Media aces : {mean_ace_2023_tournament:.2f} | std: {dev_std_aces_2023_tournament:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite giocate VS {avversario} in {TOURNAMENT}: {n_matches_2023_tournament_vs_opp}")
print(f"  Media aces VS {avversario} in {TOURNAMENT}: {mean_ace_2023_tournament_vs_opp:.2f} | std: {dev_std_aces_2023_tournament_vs_opp:.2f}")



print(f"\n###############################################################")
print(f"#########################   2022    ###########################")
print(f"###############################################################")# Tutte le partite
print("\n---------------------  ATP  ---------------------")
print(f"  Partite giocate: {n_matches_2022}")
print(f"  Aces : {mean_ace_2022:.2f} | std: {dev_std_aces_2022:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite giocate su {SUPERFICE}: {n_matches_2022_superfice}")
print(f"  Aces su {SUPERFICE}: {mean_ace_2022_superfice:.2f} | std: {dev_std_aces_2022_superfice:.2f}")
# VS Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2022_vs_opp}")
print(f"  Aces VS {avversario}: {mean_ace_2022_vs_opp:.2f} | std: {dev_std_aces_2022_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2022_superfice_vs_opp}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2022_superfice_vs_opp:.2f} | std: {dev_std_aces_2022_superfice_vs_opp:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2022}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2022:.2f} | std: {dev_std_ace_ubitiAvversario_2022_aces:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2022}): {mean_ace__subitiAvversario_surface_2022:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2022_aces:.2f}")


# Grandi Slam
print("\n\n--------------  GRANDI SLAM  --------------")
print(f"  Partite giocate: {n_matches_2022_gSlam}")
print(f"  Media aces : {mean_ace_2022_gSlam:.2f} | std: {dev_std_aces_2022_gSlam:.2f}")
# Superfice
print(f"\n- SUPERFICE: {SUPERFICE}")
print(f"  Partite GS giocate su {SUPERFICE}: {n_matches_2022_superfice_gSlam}")
print(f"  Media aces su {SUPERFICE}: {mean_ace_2022_superfice_gSlam:.2f} | std: {dev_std_aces_2022_superfice_gSlam:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite VS {avversario} : {n_matches_2022_gSlam_vs_opp}")
print(f"  Media aces VS {avversario}: {mean_ace_2022_gSlam_vs_opp:.2f} | std: {dev_std_aces_2022_gSlam_vs_opp:.2f}")
# Superfice e Avversario
print(f"\n- AVVERSARIO & SUPERFICE")
print(f"  Partite giocate VS {avversario} su {SUPERFICE}: {n_matches_2022_superfice_vs_opp_gSlam}")
print(f"  Media aces VS {avversario} su {SUPERFICE}: {mean_ace_2022_superfice_vs_opp_gSlam:.2f} | std: {dev_std_aces_2022_superfice_vs_opp_gSlam:.2f}")
# * ACE SUBITI AVVERSARIO
print(f"\n* ACE SUBITI AVVERSARIO")
print(f"  Partite giocate Avversario : {n_matches_subitiAvversario_2022_gSlam}")
print(f"  Media aces subiti Avversario: {mean_ace__subitiAvversario_2022_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_2022_aces_gSlam:.2f}")
print(f"  Media aces subiti Avversario su {SUPERFICE} (n° partite {n_matches_subitiAvversario_surface_2022_gSlam}): {mean_ace__subitiAvversario_surface_2022_gSlam:.2f} | std: {dev_std_ace_ubitiAvversario_surface_2022_aces:.2f}")

# Tournament
print(f"\n\n--------------  TOURNAMENT: {TOURNAMENT}  (2022)  --------------")
print(f"  Partite giocate: {n_matches_2022_tournament}")
print(f"  Media aces : {mean_ace_2022_tournament:.2f} | std: {dev_std_aces_2022_tournament:.2f}")
# Avversario
print(f"\n- AVVERSARIO: {avversario}")
print(f"  Partite giocate VS {avversario} in {TOURNAMENT}: {n_matches_2022_tournament_vs_opp}")
print(f"  Media aces VS {avversario} in {TOURNAMENT}: {mean_ace_2022_tournament_vs_opp:.2f} | std: {dev_std_aces_2022_tournament_vs_opp:.2f}")



print()