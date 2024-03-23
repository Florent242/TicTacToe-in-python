import tkinter


def message():
    print("le joueur", current_player, "a gagné")
def match_null():
    print("Match")
def switch_P():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else :
        current_player = 'X'

def verif_vict(click_ligne, click_colon):
    #detecter la victoire horizontale
    for i in range(3):
        count = 0
        current_bouton = buttons[i][click_ligne]
        
        if current_bouton['text'] == current_player:
                count += 1
            
    if count == 3:
            message()
            
            
    #detecter la victoire verticale
    count =0
    for i in range(3):
        current_bouton = buttons[i][click_colon]
        
        if current_bouton['text'] == current_player:
            count += 1
            
    if count == 3:
            message()
            
    #detecter la victoire  diagonale
    count = 0
    for i in range(3):
        
        current_bouton = buttons[i][i]
        
        if current_bouton['text'] == current_player:
            count += 1
            
        if count == 3:
            message()
            
    #detecter la victoire  diagonale inversé
    count = 0
    for i in range(3):
        
        current_bouton = buttons[2-i][i]
        
        if current_bouton['text'] == current_player:
            count += 1
            
        if count == 3:
            message()


#fonction de click
def placement_symbol(row, column):
    #Au moment du click on recupere les click
    print("click", row, column)
    
    #recuper le boutton clicker
    buttons_click = buttons[column][row]
    if buttons_click['text'] == "":
    
    #modifier le texte du boutons avec une croix
        buttons_click.config(text= current_player)
    
        verif_vict(row, column)
        switch_P()

#fonction de la grille
def draw_grid():
    for column in range(3):
        buttons_colon=[]
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 50),
                
                width=5, height=3,
                #pour clicker
                command=lambda r=row, c=column: placement_symbol(r, c)
                )
            button.grid(row=row, column=column)
            buttons_colon.append(button)
        buttons.append(buttons_colon)
        
#variables de stockage des bouttons
buttons = []
current_player = 'X'


# fenetre du jeu
root = tkinter.Tk()

#Personnalisation de la fenetre

#taille de la fenetre
root.minsize(500, 500)
#titre de la fenetre 
root.title("TicTacToe")



draw_grid()
root.mainloop()