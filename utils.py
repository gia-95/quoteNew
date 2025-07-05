def df_ace (giocatore, df_match, grandSlam=False) :
    # Partite giocatore
    df_giocatore = df_match[(df_match['winner_name'] == giocatore) | (df_match['loser_name'] == giocatore)]
    
    # Elimina Grandi Slam (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]
    
    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']]

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    return df_aces 

def df_ace_vs_opponent(giocatore, avversario, df_match, grandSlam=False):
    # Partite tra giocatore e avversario
    df_giocatore = df_match[
        ((df_match['winner_name'] == giocatore) & (df_match['loser_name'] == avversario)) |
        ((df_match['winner_name'] == avversario) & (df_match['loser_name'] == giocatore))
    ]
    
    # Elimina Grandi Slam (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]

    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'tourney_name', 'surface', 'best_of', 'winner_name', 'loser_name', 'w_ace', 'l_ace']].copy()

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    
    # if (len(df_aces != 0 )) :
    #     print(f"PARTITE CONTRO AVVERSARIO ({df_aces['tourney_id'].iloc[0][:4]})")
    #     print(df_aces, "\n")
    
    # print(df_aces)  
          
    return df_aces

def df_ace_surface (giocatore, df_match, surface, grandSlam=False) :
    # Partite giocatore
    df_giocatore = df_match[(df_match['winner_name'] == giocatore) | (df_match['loser_name'] == giocatore)]
    
    # Filtra su SUPERFICE
    df_giocatore = df_giocatore[df_giocatore['surface'] == surface]

    # Elimina Grandi Slam (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]
    
    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'tourney_name', 'surface', 'best_of', 'winner_name', 'loser_name', 'w_ace', 'l_ace']]

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    
    # if (len(df_aces != 0 )) :
    #     print(f"PARTITE SU SUPERFICE ({df_aces['tourney_id'].iloc[0][:4]}) ({('GS' if grandSlam  else 'non GS')})")
    #     print(df_aces, "\n")
        
    return df_aces 

def df_ace_superfice_vs_opponent(giocatore, avversario, df_match, surface, grandSlam=False):
    # Partite tra giocatore e avversario
    df_giocatore = df_match[
        ((df_match['winner_name'] == giocatore) & (df_match['loser_name'] == avversario)) |
        ((df_match['winner_name'] == avversario) & (df_match['loser_name'] == giocatore))
    ]
    
    # Filtra su SUPERFICE
    df_giocatore = df_giocatore[df_giocatore['surface'] == surface]
    
    # Elimina Grandi Slam (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]
    
    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']].copy()

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    
    return df_aces

def df_ace_tournament (giocatore, df_match, tournament) :
    # Partite giocatore
    df_giocatore = df_match[(df_match['winner_name'] == giocatore) | (df_match['loser_name'] == giocatore)]
    
    # Filtra su Tournament
    df_giocatore = df_giocatore[df_giocatore['tourney_name'] == tournament]
    
    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']]
    

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    
    return df_aces 

def df_ace_tournament_vs_opponent(giocatore, avversario, df_match, tournament):
    # Partite tra giocatore e avversario
    df_giocatore = df_match[
        ((df_match['winner_name'] == giocatore) & (df_match['loser_name'] == avversario)) |
        ((df_match['winner_name'] == avversario) & (df_match['loser_name'] == giocatore))
    ]
    
    # Filtra su Tournament
    df_giocatore = df_giocatore[df_giocatore['tourney_name'] == tournament]

    # Filtra colonne aces
    df_aces = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']].copy()

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces['aces_giocatore'] = df_aces.apply(
        lambda row: row['w_ace'] if row['winner_name'] == giocatore else row['l_ace'], axis=1
    )
    
    return df_aces

def df_ace_subiti_avversario(avversario, df_match, grandSlam=False) :
    # Partite giocatore
    df_giocatore = df_match[(df_match['winner_name'] == avversario) | (df_match['loser_name'] == avversario)]
    
    # Elimina Grandi Slam (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]
    
    # Filtra colonne aces
    df_aces_subAvversario = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']]

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces_subAvversario['aces_giocatore'] = df_aces_subAvversario.apply(
        lambda row: row['w_ace'] if row['winner_name'] == avversario else row['l_ace'], axis=1
    )
    
    if (len(df_aces_subAvversario != 0 )) :
        print(f"PARTITE AVVERSARIO({df_aces_subAvversario['tourney_id'].iloc[0][:4]}) ({('GS' if grandSlam  else 'non GS')})")
        print(df_aces_subAvversario, "\n")
        
    return df_aces_subAvversario 

def df_ace_subiti_avversario_surface(avversario, df_match, surface, grandSlam=False) :
    # Partite giocatore
    df_giocatore = df_match[(df_match['winner_name'] == avversario) | (df_match['loser_name'] == avversario)]
    
    # (best_of = 3)
    df_giocatore = df_giocatore[df_giocatore['best_of'] == (3 if grandSlam == False else 5)]
    
    # Filtra su SUPERFICE
    df_giocatore = df_giocatore[df_giocatore['surface'] == surface]
    
    # Filtra colonne aces
    df_aces_subAvversario = df_giocatore[['tourney_id', 'winner_name', 'loser_name', 'w_ace', 'l_ace']]

    # Crea una colonna 'aces_giocatore' con il numero di ace fatti dal giocatore
    df_aces_subAvversario['aces_giocatore'] = df_aces_subAvversario.apply(
        lambda row: row['w_ace'] if row['winner_name'] == avversario else row['l_ace'], axis=1
    )
    
    # if (len(df_aces_subAvversario != 0 )) :
    #     print(f"PARTITE AVVERSARIO SU SUPERFICE ({df_aces_subAvversario['tourney_id'].iloc[0][:4]}) ({('GS' if grandSlam  else 'non GS')})")
    #     print(df_aces_subAvversario, "\n")
        
    return df_aces_subAvversario

