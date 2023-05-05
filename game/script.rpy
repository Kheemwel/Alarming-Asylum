define hungry_flag = False
define window_scene = None

default player_score = 0
default computer_score = 0
default rps_win = False
default only_rock = 0
default only_paper = 0
default only_scissors = 0

default played_rps = False

transform truecenter_blur:
    xalign 0.5
    yalign 0.5
    blur 5

label start:
    $ quick_menu = True
    show black
    with noise
    
    window auto
    "…"
    show text _("{i}\"Wake up.\"{/i}") at truecenter_blur with noise
    "An inaudible voice murmurs towards me."
    "..."
    show text _("{i}\"You there, [Main]?\"{/i}") at truecenter_blur with noise
    "...Huh?"
    show text _("{i}\"Hey, wake up.\"{/i}") at truecenter_blur with noise
    "..."
    "I open my mouth but nothing comes out of it."
    show text _("{i}\"Maybe I shouldn't wake [Main] up...\"{/i}") at truecenter_blur with noise
    "I feel like I'm slipping in and out of consciousness..."
    "What do they want from me?"
    show text _("{i}\"Hello? Earth to [Main]?\"{/i}") at truecenter_blur with noise
    "What..."
    show text _("{i}\"This sleepyhead...\"{/i}") at truecenter_blur with noise
    "Hurghh..."
    show text _("{sc=10}{size=+500}WAKE UP{/size}{/sc}") at truecenter 

    window hide(None)
    pause 0.2
    stop music
    hide text

    window show(None)
    play ambient train volume 0.6 loop

    #shaky train camera
    camera:
        pause 0.5
        choice:
            pause 1.0
        choice:
            easeout_back 0.5 yoffset -10
            easein_bounce 0.5 yoffset 0
        choice:
            easeout_back 0.5 yoffset -5
            easein_bounce 0.5 yoffset 0
        pause 0.5
        repeat
    
    #bg train1
    show train1
    show forestbackground behind train1:
        xalign 1.0
        linear 1 xalign 0.0
        repeat
    window auto

    $ achievement_get("start")

    show merah neutral
    i "Wh-wha?"
    "Something hard hit my face, causing me to jerk out."
    $ a1_name = "???" 
    a1 "[Main], wake up!"
    a1 "And I thought I was the sleepy one..."
    "My eyes start to dart around to look at what's familiar and what isn't."
    $ a1_name = "Alonso" 
    i "Sorry Alonso, I must have dozed off."
    a1 "I tried waking you up earlier, but you wouldn't budge."
    "I know Alonso's a great friend, but he shouldn't just wake people up."
    "Unless it's an emergency."
    "Stretching to gain energy, I stare blankly at the window, looking for an ounce of motivation."
    a1 "Were you sleeping here alone?"
    a1 "There's plenty of seats to sleep from our side though."
    i "I don't like people watching me sleep."
    i "Even if we're the only ones here."
    "..."
    "I think there's something we both wanted to say."
    "I don't have the courage to, not yet."
    "Thankfully, Alonso breaks the silence."
    a1 "Well... aren't you excited?"
    i "I'm excited to leave once everything is over."
    "I scoffed then gave him a disapproval look."
    "He isn't that bad, he just looks after my wellbeing."
    "I mean, that's what friends do, right?"
    a1 "I'm having second thoughts about going on this trip..."
    i "What?"
    a1 "W-wait! I-it's not like that or anything..."
    "I can see right through him. Typical Alonso."
    i "We're only there to discover the mystery of the asylum."
    i "It was supposedly to be your butler's mission, but I don't know why you had to bring yourself and us as well."
    i "Heck, why did you even disclose this information to us?"
    a1 "Hold on! Just let me explain."
    a1 "What if something bad happens to her?"
    a1 "We won't be there for her."
    a1 "I know to myself I can't do it alone, so I brought you guys."
    "I paused."
    "I didn't realized how important his butler is to him."
    i "Right. Sorry, I didn't know..."
    i "But we're going to be fine. Didn't you said that before?"
    i "Whether if we encounter something paranormal or not, we've got each other."
    a1 "Yeah, you're right..."
    "..."
    "I try to yawn discreetly into my hand, but I guess it doesn't look discreet enough."
    a1 "Have you been taking your vitamins like I told you?"
    a1 "You won't last long in trips like these."
    i "Oh, I keep forgetting it."
    "Alonso scoffs at me with worry."
    a1 "You should probably start packing up."
    i "Yeah, good idea. We might be close already."
    "I rummaged through my bag to see if I already have the necessities."
    "Do I have everything in here?"
    "Flashlight, check."
    "Phone, check."
    "Food, check."
    "Notebook, check."
    
    "Gun, chec{nw}"
    $ _history_list[-1].what = "Self-defense items, check."
    $ del _history_list[-2:]
    "Wait, what?{fast}"
    $ del _history_list[-1:]

    "Right, first-aid... check."
    "I leave my warm seat in a haste and drag all of my belongings with me."
    i "I guess I have everything right here."
    a1 "Alright, I'll go with the others. Care to join us?"
    menu:
        "Err..."
        "\"Sure.\"":
            a1 "Okay. Right this way."
            "We left the current passenger wagon onto the other one."
            window hide
            hide train1
            show train2 behind merah
            with wipeleft_scene
            window auto
            jump char_intro
        "\"No thanks, I need some more time alone.\"":
            a1 "Suit yourself."
            hide merah
            "Alonso leaves the scene, giving the passenger wagon to myself all alone."
            "Dammit. I forgot to eat lunch."
            "I was hoping they'd at least offer some food here."
            
            menu:
                "Should I eat the food I brought along now?"
                "Yes.":
                    "Can't start the day with an empty stomach, right?"
                    "*munch*{w=1.5} *munch*{w=1.5} *munch*"
                    pause 1.0
                    window auto
                    
                "No.":
                    "Keep it together, [Main]."
                    "Just a few more minutes and this trip will be over."
                    "I have to save my food for the worst."
                    $ hungry_flag = True

            "I think getting some fresh air would ease me off."
            "I open the window."
            "Suprisingly, the wind against my face is actually rather pleasant."
            menu:
                "Should I...?"
                "Peek outside.":
                    "I peek a bit outside the window frame."
                    hide train1
                    show forestbackground:
                        yoffset 250
                        xalign 1.0
                        linear 1 xalign 0.0
                        repeat
                    with dissolve
                    "The scenery whizzed by in a blur of green and brown."
                    "I feel a sense of freedom and exhilaration that only comes from being on the move."
                    "It's a bit chilly, but in a good way. I feel myself waking up even more."
                    "I savored the simple pleasure of the wind, feeling the coolness and the rush of the air against on my face."
                    "I'd like to forget about my worries and cares, just for a moment."
                    window hide
                    show screen slow_text_center("{bt=h5-p2.0-s0.5}{size=+35}Ahhh...{/bt}")
                    pause 5.0
                    hide screen slow_text_center with Dissolve(3.0)
                    $ window_scene = True
                "Stay in.":
                    "I don't think I should. I might fall."
                    "I'll just look at the scenery."
                    window hide
                    pause 5.0
                    $ window_scene = False
    

    label char_intro:
        if window_scene == True:
            show train1
            show forestbackground behind train1:
                yoffset 0
                xalign 1.0
                linear 1 xalign 0.0
                repeat
            window show(None)
            a1 "{size=+50}[Main!u]!{/size}{fast}" with vpunch
            window auto
            i "Gah! What th-{nw}" with vpunch
            i "Don't sneak behind me like that!"
            a1 "Hehe, sorry."
            "..."
            i "Alonso... Please don't do that again."
            a1 "Right, right. I'm sorry I scared you."
            # "Flabbergasted, I went back gazing into the distance."
            a1 "Oh! My butler wants to see you."
            a1 "I don't know what it is, but I'll leave the two of you alone."
            i "Is that so?"
        elif window_scene == False:
            window auto
            "I wonder..."
            "What made the asylum haunted."
            "It's not something I should be worried of... right?"
        else:
            window auto
            a1 "Stay here while I look for Raymon."
            i "Okay."
            hide merah
            "I scanned the whole area."

        "In the corner of my eye, I see a well-suited lady approaching me."
        show lucy with Dissolve(0.2)
        $ l1_name = "???"
        lucy "Greetings, [Main]."
        $ l1_name = "Lucy" 
        i "Oh. Hello Ms. Lucy."
        show lucy l_base3
        lucy l_eyes_closed "Please, Lucy is fine."
        play music merrygoround
        "We head on an empty train seat that comes along with a table."

        if hungry_flag == True:
            hide lucy with Dissolve(0.2)
            "As I approach the table, she goes back to the kitchen."
            "Wait, do trains have kitchens?"
            "I'm amazed on how Lucy decides to cook on times like these. Even on her mission."
            "..."
            "I lightly shake my head." with hpunch
            "That's not important! I'm more invested on what Lucy has in store for me."
            "The scent alone coming from the kitchen swiftly made its way to my nose."
            "It smells so good that the scent alone makes me drool."
            "Soon after, Lucy comes out of the kitchen as she brings my plate."
            show lucy l_base3 l_brow_sad with Dissolve(0.2)
            lucy "I noticed that you look off today..."
            lucy -l_brow_sad l_eyes_closed -l_base3 "So I prepared you some food."
            show lucy -l_eyes_closed
            "..."
            "I struggle to come up with any words. My mind is focused entirely on Lucy's plate."
            lucy l_base3 l_brow_sad l_mouth_serious "Hello? Are you still there, [Main]?"
            show lucy l_brow_sad -l_mouth_serious
            i "O-oh. Sorry."
            show lucy -l_base3 l_eyes_closedhappy -l_mouth_serious -l_brow_sad
            "Lucy chuckles back as she offers the plate in front of me."
            lucy -l_eyes_closed"What are you waiting for? Eat."
            i "T-thank you for the food!"
            show lucy l_eyes_closed
            "Surprisingly, the food tastes pretty good."
            "I can't tell what some of the spices are, but they blend together nicely."

            if window_scene == True:
                i "It would be nice if the window was open."
                lucy l_mouth_slightopen -l_eyes_closed "Is that so?"
                i "I did something like that earlier."
                lucy l_eyes_look l_base2 -l_mouth_slightopen l_brow_sad"I too would have loved it."
                lucy l_eyes_closed -l_brow_sad l_mouth_serious"But your food would easily get cold, so I would not recommend it."
                hide lucy
                show lucy
                i "Oh, okay."
            else:
                pass

        else:
            hide lucy
            show lucy
            "Lucy pours a glass of what it seems to be water and offers it to me. It's fizzing a bit, and almost looks carbonated."
            "I give it a sniff. It smells kind of fruity."
            show lucy -l_base3
            lucy -l_eyes_closed "Go ahead, you look thirsty."
            i "Thanks. I've been needing it."
            "I take a sip on the water."
            show lucy l_eyes_closed
            "The fizzing sensation of the water soothes my dried mouth."
            "As I gaze on her, she traces the rim of her teacup with her fingertip."
            "..."
            "Not being sure what to say to her, I stay silent, hoping that she would say something else soon."
            "In which, an awkward silence formed between us."
            "I feel so hopeless that I can't come up with anything to say."
            "..."
            i "So Lucy, h-how are you?"
            show lucy l_mouth_slightopen
            show lucy -l_eyes_closed
            "Wow [Main], what a great start."
            lucy -l_mouth_slightopen "I am doing fine."
            show lucy l_eyes_closed
            lucy "I find the train ambience quite calming."

            if window_scene == True:
                i "Not as calm as opening a window. I did something like that earlier."
                lucy l_mouth_slightopen -l_eyes_closed "Is that so?"
                show lucy -l_mouth_slightopen l_base2
                lucy l_brow_sad l_eyes_look "I would probably do something so carefree like that..."
                lucy l_eyes_closed "If you didn't do it earlier."
                lucy -l_eyes_closed "You were sightseeing."
                show lucy l_base3
                lucy l_brow_sad l_eyes_closed "And I would not want it to be ruined so I left you alone."
                show lucy -l_base3 -l_eyes_closed
                i "O-oh. I see..."
                "So she saw me."
                i "Thanks for letting me have a moment for myself."
                lucy l_eyes_closedhappy -l_brow_sad "My pleasure."
                show lucy -l_eyes_closedhappy
            else:
                "I focus my hearing on the surroundings."
                "She's right. It does feel relaxing."
                "I look at myself in the window..."
                "...just to see the scene at the distance nearing towards us."
                lucy -l_eyes_closed"Do you want me to open the window?"
                lucy "Surely the breeze would make you feel a bit better."
                i "Oh, sure. Go ahead."
                "Lucy opens the window."
                "Suprisingly, the wind against my face is actually rather pleasant."

        window hide
        pause 3.0
        window auto

        "Where does she even get the determination to deal with our stupidity?"
        "She's quite an amazing woman. Matured, independent..."
        "I can never be as good as her."
        "She has also never shown any vulnerabilities since we've met her."
        "On second thought..."
        i "How do you do it?"
        lucy l_mouth_slightopen -l_eyes_closed"Do what?"
        i "You know, deal with us. Our group is vast, each with their own unique personalities."
        i "I'm surprised that you can manage to adjust according to our interests."
        show lucy l_base3 l_eyes_closedhappy -l_mouth_slightopen
        "Lucy giggles from my compliment."
        lucy l_eyes_closed"I have seen the world far more than you know."
        i "Really? What of it?"
        lucy -l_eyes_closed "Oh, a lot. You will be surprised at what I can do."

        if hungry_flag == False:
            lucy l_eyes_look l_brow_sad "Maybe cook, I suppose?"
            lucy l_mouth_open -l_brow_sad l_eyes_closedhappy"Ahaha."
        else:
            lucy l_eyes_look l_brow_sad "Maybe share someone with a drink and enjoy the scenes unfold from the window?"
            lucy l_eyes_closedhappy -l_brow_sad"That would be nice..."

        i "I see." 
        show lucy l_eyes_closed -l_brow_sad -l_mouth_open l_base1
        "I've always wondered why she's always looking after us."
        "I get that she IS Alonso's butler."
        "There's no harm in asking her, right?"
        i "Why do you also look after us?"
        show lucy -l_eyes_closed
        i "Shouldn't you only serve Alonso?"
        show lucy l_mouth_serious l_brow_serious
        $ renpy.music.set_volume(0.0, delay=0.0, channel='music')
        "Lucy's expression immediately changed."
        "I might have strike a nerve."
        lucy l_mouth_slightopen "A friend of Alonso is also my responsibility."
        lucy l_eyes_closed l_base3"It is something that we, servants, should also serve."
        show lucy l_mouth_serious -l_base3 -l_eyes_closed
        "Right, a butler's expertise."
        "That was a stupid question to ask."
        i "I didn't mean it like that. I'm sorry."
        $ renpy.music.set_volume(1.0, delay=0.0, channel='music')
        lucy l_brow_sad l_eyes_look l_base3 -l_mouth_serious "I know you do."
        lucy l_eyes_closed"And I apologize for acting out so sudddenly."
        lucy -l_eyes_closed -l_base3 "Now, why don't you go with the others?"
        i "Okay..."
        hide lucy with Dissolve(0.2)
        "Just as I leave Lucy, I looked back at her with sincerity."
        show lucy l_mouth_serious l_brow_serious with Dissolve(0.2)
        i "By the way..."
        show lucy l_mouth_slightopen -l_brow_serious
        i "Thanks Lucy."
        show lucy l_brow_sad -l_mouth_slightopen
        extend "\nFor everything."
        i "Realizing your state, I guess you we should thank you for looking after us."
        show lucy l_eyes_closedhappy -l_brow_sad
        "Lucy smiles genuinely at me as she continues cleaning up. I smile back naturally, leaving her."
        hide lucy with Dissolve(0.2)
        "I let out another yawn and start to glance around the room."
        "So, where are they?"
        "I walked through the long corridors of the passenger wagon to find Alonso."
        "Though I seem to stumble upon a small reading place in the corner of the carriage."
        "The bookshelves are displayed in a minimalistic manner; categorized neatly with books of all genres along a beanbag on the floor."
        "This train sure has everything!"
        "I made my way over to the area and began scanning the titles."
        "Suddenly, my eye caught a person; fully immersed in their book."

        $ m2_name = '???'
        show raymon with Dissolve(0.2)
        raymon "Oh, hi [Main]."
        $ m2_name = 'Raymon'
        i "Hey, Raymon."
        "Raymon had always been a bookworm with a twist."
        "He loved the way books transported him to other worlds, filled his mind with new ideas, and gave him a sense of purpose."
        raymon r_mouth_open "Care to read some books with me?"
        i "Sure."
        show raymon -r_mouth_open
        "He's surrounded with books ranging from literature to... manga?"
        "He surely has everything."
        raymon r_brow_sad r_mouth_serious "Sorry about that, all the seats been taken by the books."
        hide raymon
        show raymon
        "Raymon whips out a portable beanbag out from his bag."
        show raymon r_eyes_closedhappy
        "That's the twist."
        "He always comes prepared."
        "Where did that even come from?"
        raymon r_eyes_closed "I know, I've come prepared for this moment."
        show raymon -r_eyes_closed
        "Raymon showed me some of his favorite books, from classic novels to modern memoirs."
        raymon r_mouth_slightopen "I've actually read in advanced about the asylum's past."
        raymon "There's a lot to take in."
        show raymon -r_mouth_slightopen
        i "I-is that so?"
        i "I never thought you'd come prepared."
        raymon r_eyes_closedhappy r_mouth_open "Of course! I'm always prepared."
        i "So, what made you take all of the books here?"
        raymon -r_eyes_closedhappy "I find reading a bit mesmerizing. So I took the books that caught my attention."
        raymon "I then imagine myself being at the shoes of the main character."
        raymon -r_mouth_open "Ooh, about that..."
        raymon r_eyes_closed r_mouth_slightopen"A certain book caught my attention yesterday and I was hoping to read it with someone here."
        raymon -r_mouth_slightopen -r_eyes_closed"It's about a group of friends traveling in an abandoned mansion."
        raymon r_brow_sad r_eyes_closed r_mouth_serious "Where... you guessed it, someone had to die."
        raymon "If only he had accepted that her death was inevitable. I always think of different ways on how the story could have gone to."
        raymon r_eyes_look "The way of he enunciated his feelings to the other characters..."
        $ renpy.music.set_volume(0.2, delay=5.0, channel='music')
        show raymon -r_eyes_look r_mouth_open -r_brow_sad
        "I could see the excitement in his eyes and the way his voice became animated when he talked about his favorite books."
        show raymon r_eyes_closedhappy
        "I sometimes couldn't even comprehend his usage of words."
        show raymon r_eyes_closed r_mouth_slightopen
        "I mean, he tries his best to make it comprehensible for us..."
        show raymon r_brow_sad
        "Which... ends up poorly executed."
        show raymon r_eyes_look r_mouth_serious
        "I have to search my phone to find the definitions of his words."
        "He reminds me of a person who uses sugarcoating on his essa{nw}"
        $ _history_list[-1].what = "He reminds me of someone I used to know somewhere else."
        $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
        raymon "... then left all alone in the world with nothing but himself because he did not follow the order."
        raymon r_eyes_closed"..."
        show raymon -r_eyes_closed -r_brow_sad r_mouth_slightopen
        "He paused for a moment, realizing he had been talking alone."
        raymon r_eyes_look r_mouth_open r_brow_sad"Sorry, I must be rambling again..."
        i "No no, it's fine!"
        hide raymon
        show raymon
        i "I like the way..."
        i "The uhh..."
        show raymon r_mouth_serious
        i "Uhm..."
        i "..."
        "Oh crap, I was lost in thought!"
        raymon r_eyes_closed r_brow_sad"It's fine anyway. The book was too much for you, wasn't it?"
        raymon -r_eyes_closed -r_brow_sad"You wouldn't like it anyway."
        "He gives me a disappointing look."
        "I try to come up some excuse to make the situation less awkward."
        i "I-I mean, we can learn some crucial tips from that book of yours."
        i "Maybe if that happens to us, we can prevent death?"
        raymon r_eyes_closedhappy r_mouth_open"Ahaha!"
        raymon "What kind of analogy is that?"
        $ renpy.music.set_volume(0.0, delay=0.0, channel='music')
        raymon -r_mouth_open -r_eyes_closedhappy "This is fiction. That wouldn't happen to us."
        "For some reason, I felt a chill down my spine after hearing that."
        "I couldn't help but feel a sense of foreboding."
        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        raymon "The book, I mean."
        raymon r_eyes_closed r_brow_sad"I have always wanted to embark in an abandoned haven..."
        raymon r_eyes_look r_mouth_open "That is, if you can still label it that..."
        i "I'm not really liking the concept of us going through a haunted house."
        raymon r_brow_serious r_mouth_serious -r_eyes_look "It's not a haunted house. It's an abandoned sanctuary."
        raymon r_eyes_closed -r_brow_serious "We're essentially making history here by unraveling the secrets of the asylum."
        raymon -r_eyes_closed r_mouth_open "I even brought a vintage camera to capture the essence of our journey!"
        raymon r_eyes_closedhappy "Isn't that fun?"
        i "Of course, that's something that you like."
        "I can already see the determination from his eyes."
        raymon r_mouth_slightopen r_eyes_look "Oh, there's Alonso and Lucy. Just in time."
        hide raymon with Dissolve(0.2)
        show lucy at left
        show merah neutral at right
        with Dissolve(0.2)
        a1 "There you are [Main]!"
        a1 "Man, wandering through these empty endless passenger wagons sure is tiring."
        a1 "I've been looking everywhere for you two."
        "How did he get lost? This train is just a corridor..."
        a1 "Luckily, I came across Lucy. She pointed out exactly where you guys are."
        i "Thanks, Lucy. If it weren't for you, Alonso would've been left wandering aimlessly in the train."
        show lucy l_base2 l_mouth_open l_eyes_closedhappy 
        "Lucy laughs from my bad-executed joke."
        a1 "Yeah yeah, laugh it off."
        hide lucy
        show lucy at left
        a1 "I'll laugh once I beat [Main] in this game!"
        a1 "How about a game of rock, paper, scissors for a while?"
        label menu_rps:
            menu:
                a1 "Best of 3?"
                "\"Sure, we're almost there anyway.\"":
                    $ played_rps = True
                    a1 "Alright!"
                    jump rps
                "\"No thanks.\"":
                    a1 "Aww."
                    jump afterwards
                "\"What are you, a kid?\"" if persistent.easter_egg1 == None:
                    a1 "Aww."
                    a1 "That really hurt."
                    a1 "I mean, that's the only minigame they can implement."
                    a1 "Have some respect."
                    "Huh? What minigame?"
                    i "Who's they?"
                    a1 "The developers. The people who made this game."
                    i "What are you talking about?"
                    a1 "They're watching us right now."
                    show forestbackground:
                        xalign 0.0
                        linear 1 xalign 1.0
                        repeat
                    show layer master at rewind
                    show skip_overlay
                    $ quick_menu = False
                    $ config.skipping = False
                    $ config.allow_skipping = False
                    $ renpy.music.set_volume(0.0, delay=0.0, channel='music')
                    play sound "audio/bgm/merrygoround_reverse.mp3"
                    "{cps=150}What are you talking about?{/cps}{nw}"
                    a1 "{cps=150}The developers. The people who made this game.{/cps}{nw}"
                    i "{cps=150}{/cps}Who's they?{nw}"
                    "{cps=150}Huh? What minigame?{/cps}{nw}"
                    a1 "{cps=150}Have some respect.{/cps}{nw}"
                    a1 "{cps=150}I mean, that's the only minigame they can implement.{/cps}{nw}"
                    a1 "{cps=150}That really hurt.{/cps}{nw}"
                    a1 "{cps=150}Aww.{/cps}{nw}"
                    hide skip_overlay
                    show layer master
                    stop sound
                    $ renpy.music.set_volume(1.0, delay=0.0, channel='music')
                    $ persistent.easter_egg1 = True
                    $ del _history_list[-18:]
                    $ achievement_get("doki_doki")
                    $ config.allow_skipping = True
                    $ quick_menu = True
                    show forestbackground:
                        xalign 1.0
                        linear 1 xalign 0.0
                        repeat
                    jump menu_rps
                    

    label rps:
        $ config.skipping = False
        if player_score == 3:
            $ rps_win = True
            jump results
        elif computer_score == 3:
            jump results
        elif player_score == 2 and computer_score == 2:
            a1 "It's now or never!"
        else:
            pass
        show screen scoring with Dissolve(0.25)
        call screen rps_screen with Dissolve(0.25)
        $ player_selection = _return
        $ computer_selection = renpy.random.choice(['rock', 'paper', 'scissors'])
        pause 0.5
        show text _("{size=+100}ROCK...{/size}") with Dissolve(0.1)
        pause 0.5
        show text _("{size=+100}PAPER...{/size}")
        pause 0.5
        show text _("{size=+100}SCISSORS...{/size}")
        pause 0.5
        show text _("{sc=10}{size=+500}GO!!!{/size}{/sc}")
        pause 0.5
        hide text with Dissolve(0.1)
        "I chose [player_selection] and Alonso whips out [computer_selection]."

        if player_selection == computer_selection:
            "It's a tie."
            a1 "Ooh, I'll get ya!"
            jump rps

        elif player_selection == 'rock':
            if computer_selection == 'scissors':
                $ only_rock += 1
                $ only_paper = 0
                $ only_scissors = 0
                $ player_score +=1
                "Rock beats scissors! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Paper beats rock! I lost!"
                jump rps

        elif player_selection == 'paper':
            if computer_selection == 'rock':
                $ only_paper += 1
                $ only_rock = 0
                $ only_scissors = 0
                $ player_score +=1
                "Paper beats rock! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Scissors beats paper! I lost!"
                jump rps

        elif player_selection == 'scissors':
            if computer_selection == 'paper':
                $ only_scissors += 1
                $ only_paper = 0
                $ only_rock = 0
                $ player_score +=1
                "Scissors beats paper! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Rocks beats scissors! I lost!"
                jump rps
        
    label results:
        if rps_win:
            $ achievement_get("rps_game")
            i "I win."

            if only_scissors >= 3:
                $ achievement_get("rps_game_scissors")
                i "And I beat you using [player_selection]!"
            
            elif only_rock >= 3:
                $ achievement_get("rps_game_rock")
                i "And I beat you using [player_selection]!"

            elif only_paper >= 3:
                $ achievement_get("rps_game_paper")
                i "And I beat you using [player_selection]!"
            
            i "Take that!"
            if only_paper >=3 or only_rock >=3 or only_scissors >=3:
                a1 "Yeah yeah, rub it in. That was pure luck."
            else:
                a1 "I'll get you next time..."
            jump afterwards
        else:
            i "Aww, I lost."
            a1 "Bow to me!"
            jump afterwards

    label afterwards:
        hide screen scoring with Dissolve(0.25)
        stop music fadeout 10.0
        play sound "audio/sfx/announce.mp3" volume 0.3
        "{i}\"Attention, passengers: this is your conductor speaking.\"{/i}"
        "{i}\"We are now arriving at the train stop shortly.\"{/i}"
        "{i}\"Passengers are reminded to mind the gap between the train and the platform edge when unboarding.\"{/i}"
        "{i}\"Thank you and have a nice day.\"{/i}"
        if played_rps == True:
            raymon "While you guys are playing your game, me and Lucy have packed your things up, thank you very much."
            a1 "Whoops, thanks."
        else:
            a1 "Whaddya know. We're here."
        a1 "Do you have everything with you, [Main]?"
        "I'm not sure if I left anything at the seat I was sleeping in..."
        "If there's anything I left behind, so be it."
        i "I guess I'm all good now."
        a1 "Great! Let's go."
        stop ambient fadeout 6.0
        play sound trainstop
        window hide
        camera
        show forestbackground with dissolve:
            xalign 1.0
            linear 1 xalign 0.0
            xalign 1.0
            linear 1.5 xalign 0.0
            xalign 1.0
            linear 2.0 xalign 0.0
            xalign 1.0
            linear 2.5 xalign 0.0
            xalign 1.0
            easein 3.0 xalign 0.0
        pause 10.0
        
        window auto
        scene bg trainstation with wipeleft_scene
        play ambient forest loop fadein 2.5
        i "We're here."
        "..."
        "I scanned the whole area."
        "There's nothing but trees and bushes as far as my eyes can see."
        "The sun is shining along with the birds singing, but the forest is eerily quiet."
        "Too quiet..."
        i "Um, where is the asylum?"
        lucy "Patience, [Main]. We are not there yet."
        lucy "We have to traverse through the forest."
        a1 "Adventure awaits us!" with vpunch
        "Alonso comes near me, and reaches his hand to me."
        a1 "Come along, my companion."
        i "What's up with that attitude of yours?"
        a1 "Aw, can you just appreciate my enthusiasm?"
        a1 "I'm trying to make this trip a bit fun."
        "This trip is going to be the end of me."
        i "Do you even know where're we going?"
        a1 "Err... no?"
        "I {bt=1}sighed{/bt}."
        raymon "Why don't we let Lucy lead the way?"
        raymon "She WAS assigned to this mission after all."
        i "That would make more sense."
        a1 "R-right."
        "Lucy goes in front of us and giggles as she takes the lead."
        scene bg forest1 with wipeleft_scene:
            yalign 1.0
            linear 300 yalign 0.0
        play sound "audio/sfx/walking.mp3" loop volume 0.1
        "We followed a narrow trail, with trees looming over us on either side."
        i "Wow, this place must be really hidden from the public."
        i "It must be a refugee site for individuals from other states."
        raymon "No. It wasn't."
        # raymon "Hey Lucy, what kind of {i}\'asylum\'{/i} are we going to anyway?"
        # raymon "Is it a rehabilitation center to treat the lunatics in nuthouses or a refugee site?"
        lucy "..."
        "Lucy remained silent."
        "I think she's trying to say something, but doesn't know how to respond yet."
        show black:
            alpha 0.0
            linear 20 alpha 0.7
        # lucy "There is a reserved section for lunatics, but that was in the basement; forgotten."
        # lucy "Mostly, the ground floors and upper floors were assigned to give shelter to asylum seekers."
        # lucy "But for some unknown reasons, none of refugees were recorded to be released."
        # lucy "I am guessing all the refugees were taken to the basement along with the lunatics."
        lucy "Asylums were used as a form of social control, with individuals who did not conform to societal norms or who were perceived as a threat to public safety, often being institutionalized."
        lucy "As a result, many patients suffered and died in those institutions, with their stories and struggles forgotten."
        lucy "It is also a place where they performed... human experiments."
        lucy "Patients were often subjected to inhumane treatments such as lobotomies, electroshock therapy, and other experimental procedures."
        raymon "And patients with mental illnesses were often mistreated by society at large, leading to a lack of proper care and support."
        lucy "Exactly."
        # lucy "It is probably the reason why the asylum was built here."
        # lucy "It had been a prison for patients who had been locked away, forgotten by society."
        # lucy "Screams can be heard deep within the forest back then, and even today."
        hide black
        lucy "I might be rambling too much..."
        lucy "Surely you have heard stories about this place, [Main]?"
        i "N-no..."
        "Sort of..."
        "I'm at loss for words."
        "Even Alonso is speechless."
        "But not Raymon. I'm guessing he's read stories like these already."
        # i "Poor patients. All they wanted was a safe place..."
        # i "And what they got is--{w=0.7}{nw}"
        # raymon "...death."
        # "..."
        raymon "Where are the people running the asylum?"
        lucy "That, I do not know."
        lucy "Only God knows where they went."
        "..."
        "We decided to keep quiet for the rest of our journey."
        window hide
        scene bg forest2 with wipeleft_scene:
            yalign 0.5
        window auto
        "As we walked deeper into the forest, the atmosphere began to change."
        "The air grew cooler, and the sunlight filtered through the trees in an eerie way."
        "I could hear strange noises in the distance, and the rustling of leaves seemed to follow us."
        a1 "Are we there yet already?"
        lucy "Yes. Just a bit more."
        lucy "It should be right around the corner."
        "..."
        $ renpy.music.set_pause(True, channel="sound")
        "Lucy pauses for a moment and points out in the distance."
        lucy "Over there."
        window show
        scene bg outside_asylum:
            yalign 1.0
        with wipeleft
        window auto
        "I follow Lucy's degraded path."
        $ renpy.music.set_pause(False, channel="sound")
        show bg outside_asylum:
            yalign 1.0
            linear 5 yalign 0.70
        "It was even more imposing than I had imagined, with broken walls and shattered windows."
        stop sound fadeout 1.5
        i "Wow, we've been walking for hours."
        "It's almost night already."
        lucy "We're here."
        lucy "Before we go ahead inside, is anyone of you ready?"
        a1 "My stuff's here."
        a1 "How about you, Raymon?"
        play sound "audio/sfx/camera.mp3" volume 0.5
        "{bt=2}*click*{/bt}{fast}"
        "I see Raymon waving a plastic film, taken by his camera."
        # raymon "I can almost hear the deafening souls..."
        raymon "Of course! I'm always prepared."
        a1 "The walls look it could give up at any moment..."
        lucy "Indeed, it does."
        lucy "We might have to get this mission done as soon as possible."
        i "I'm ready."
        lucy "Then let us."
        "We approached the entrance."
        scene bg door with wipeleft_scene:
            yalign 1.0
        jump scene_2

return