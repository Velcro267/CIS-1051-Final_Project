# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("AJ", color="#c0397a")
define l = Character("Liam", color="#9772c4")


# The game starts here.

label start:

    ###Scene 1

    scene bg school_hallway2
    with fade

    #Narration
    "Ah, just another day where we find ourselves here at an undisclosed
    school, in an undiclosed city." 

    "I wonder what mundane conversations are happening in the hallway..."


    show AJ pissed 

    a "Man do I hate Mr. Soinso's class. All he does is talk about 
    vector fields and the higgs boson."
    a "Like what does any of that even have to do with African history. Just
    stick to the topic bro."

    
    l "Hey AJ, can you come over here for a sec?"

    a "Sure thing."



    ###Scene 2
    scene bg school_stairs2
    with dissolve

    show AJ neutral2 at left
    
    show Liam smile2 at right with fade

    a "Damn I be forgetting how tall you are. You barely fit in the screen."

    show Liam neutral
    l "Huh, what are you talking about?"

    show AJ happy
    a "Nothing."
 
    a "What did you want to talk about?"

    show Liam smile2
    l "Since we're done with classes for the day, would you want to go and hangout?"

    show AJ blush

    l "I know we haven't really talked at all because we just came into existence, 
    but I really want to talk outside of the couple seconds we have while crossing in the hallways."
    l "What say you?"

    a "I... uhhh..."
    a "Don't ask me something like that out of nowhere, baka."







    ###Scene 3


    # This ends the game.
    "The End"

    return
