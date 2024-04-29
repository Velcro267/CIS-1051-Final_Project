# The script of the game goes in this file.

###Characters
define a = Character("AJ", color="#c0397a")
define l = Character("Liam", color="#9772c4")


# The game starts here.

label start:

    ###Scene 1

    scene bg school_hallway2
    with fade

    play music "audio/relaxing_piano_loop.mp3" fadein 1.0 volume 0.5

    

    #Narration
    "Ah, just another day where we find ourselves here at an undisclosed
    school, in an undiclosed city." 

    "I wonder what mundane conversations are happening in the hallway..."


    show AJ pissed 

    a "Man do I hate Mr. Soinso's class. All he does is talk about 
    vector fields and the higgs boson."
    a "Like what does any of that even have to do with African history. Just
    stick to the topic bro."
    a "And why is music playing through the loud speakers? 
    Nothing seems to make sense today."

    
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


    "Since AJ can't decide her fate, you the viewer will."
    play music "tension_synths.mp3" fadein 1.5 volume 0.5

    menu:
        "Yes, I would really enjoy that!":
            jump choice1
        "Eww get away frome me.":
            jump choice2 
        "...":
            jump choice3
        "You shouldn't ask such brash questions, baka.":
            jump choice4
    
    label choice1:
        show AJ blush
        a "Yes, I would really enjoy that!"

        show Liam happy
        l "Really? Gee, willikers! I can't beileve that worked!"

        show AJ pissed 
        a "Actually, nevermind. I can't be seen talking to someone who says
        shit like that."

        show Liam apologize
        l "Oh, well alright then. "
        jump theEndingScreen
    
    label choice2:
        show AJ pissed
        a "Eww get away from me." 
        hide AJ 
        
        show Liam sad
        l "Wow... ok then."

        jump theEndingScreen
    

    label choice3:
        show AJ neutral2
        a "..."

        show Liam neutral
        l "Look if the answer is no just say that."

        a "..."

        show Liam angry
        l "Yea thanks for wasting my time."
        hide Liam 

        show AJ sad
        a "Well that was... something."

        jump theEndingScreen
    

    label choice4:
        stop music
        play sound "happy_effect.mp3"
        show AJ blush
        a "You shouldn't ask such brash questions, baka."

        show Liam sly 
        l "Soooo, is that a yes?"

        a "Yea it's a yes."

        show Liam smile2
        l "Great, well we can go now since were both done with classes!"

        show Liam neutral
        l "By the way, did you here that sound a couple seconds ago too?"

        show AJ neutral
        a "Yea werid things have been happening today. Just go with the flow."

        l "Noted."
        


    ### Scene 3
    scene bg outside_urban2
    with dissolve
    play music "future_chill_music.mp3" fadein 1.5 volume 0.5

    show AJ happy
    show Liam happy at left

    a "So what did you have in mind for us to do?"

    show Liam neutral
    l "Actually I didn't think that far ahead."

    show Liam smile2
    l "It was challenging enough to just ask you out."

    a "Oh."
    a "Well I'm down to just talk over some food while we sit outside.
    The weather is beautiful today."

    l "That sounds lovely."





    # This ends the game.

    label theEndingScreen:
        scene bg outside_urban2
        "Thus concludes our little story."
        "If you think there was nothing special about it, thats because 
        it was just another day :)"
        "The End"

        return

    return
