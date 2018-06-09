init:
    $ mateo = Character("Mateo", color="#aaaaff")
    $ wire1 = Character("Mesh 1", color="#aaffaa")
    $ wire2 = Character("WireFrame 2", color="#aaffaa")
    $ alia = Character("Cell Lord Alia", color="#aaffaa")
    $ ale = Character("Cell Lord Ale", color="#aaffaa")
    $ grace = Character("Diffuse Lord Grace", color="#aaffaa")
    $ harshini = Character("Diffuse Lord Harshini", color="#aaffaa")
    $ shenuka = Character("Phong Lord Shenuka", color="#aaffaa")
    $ norm = Character("Norm", color="#aaffaa")
    $ mal = Character("Mal", color="#aaffaa")
    $ d3p4z = Character("D3P4Z", color="#aaffaa")
    $ ukn = Character("???", color="#aaffaa")
    $ bunny = Character("Bunny", color="#aaffaa")
    $ everyone = Character("Everyone", color="#aaffaa")
    $ thirangie = Character("Thirangie", color="#aaffaa")
    $ ming = Character("Ming", color="#aaffaa")
    image bgIMLab = im.Scale("IMLab.jpg",1440, 800)
    image bgLivingRoom = im.Scale("livingroom.jpg",1440, 800)
    image bglib = im.Scale("lib.jpg",1440, 800)
    image bgIMClass = im.Scale("IMClass.jpg",1440, 800)
    image bghowler = im.Scale("howler.jpg",1440, 800)
    image bgIMClassColor = im.Scale("imclasscolor.jpg",1440, 800)
    image rabbit = im.Scale("rabbit.png",450,800)
    image rabbit2 = im.Scale("rabbit.png",450,850)
    image abdullahreg = im.Scale("abdullah.png",400,700)
    image alescared = im.Scale("alescared.png",400,700)
    image aliahappy = im.Scale("aliahappy.png",400,700)
    image gracehappy = im.Scale("gracehappy.png",400,700)
    image gracescared = im.Scale("gracescared.png",400,700)
    image harshinihappy = im.Scale("harshinihappy.png",400,700)
    image harshiniscared = im.Scale("harshiniscared.png",400,700)
    image mingreg = im.Scale("ming.png",400,700)
    image shantanureg = im.Scale("shantanusmirk.png",400,700)
    image shenukareg = im.Scale("shenukahappy.png",400,700)
    image thirangiereg = im.Scale("Thirangie.png",400,700)
    
label start:
    stop music fadeout 3.0
    play music "nostalgia.wav" fadein 2.0
    mateo "Urrgh...How long was I napping for?"
    "An ominous silence envelopes the hazy surroundings."
    mateo "Wait...where am I?"
    "The haze lifts to reveal a familiar laboratory."
    scene bgIMLab with fade
    mateo "Why am I at the IM Lab? Wasn’t I in my dorm coding shaders?"
    "It was indeed the IM lab, but something seemed off…."
    mateo "HOLD ON - WHAT THE FUCK"
    mateo "WHERE IS ALL THE COLOUR??!!?"
    ukn "There you are!"
    ukn "Mateo!"
    "Two people made only of wireframes run to you from the doorway."
    wire1 "Mateo, you're the only one who can help us!"
    wire2 "The reason everything looks like this is because there are no more shaders!"
    mateo "What......"
    mateo "..........."
    mateo "......................."
    mateo "WHAT DO YOU MEAN NO MORE SHADERSSSSSSSS?!?!?!?!?!?!?!"
    wire1 "All the shaders have been stolen from this world by an entity known only as Le Monsieur."
    wire2 "Each shader has been imprisoned in a different location, take this mip_map, it will lead you to them."
    mateo "Uhhh that’s not what a mip_map does..."
    wire1 " Dude just go with it, we’re kinda of in a situation here."
    "Do you take the mip_map anyways?"
    menu:
        "Fuck Yeah!":
            jump Yep

        "Nah, I mean I should probably work on my capstone...":
            jump Nope
label Nope:
    wire1 "Uh oh, this is unexpected..."
    wire2 "I guess we'll come back later then.."
    "A few hours later in a shaderless void.."
    wire2 "Are you ready now?"
    menu:
        "Yes":
            jump Yep
       
label Yep:
    wire1 "Good luck! And, watch out for Le Monsieur, he is very powerful and dangerous!"
    wire2 "Especially with his all consuming sass!"
    wire1 "We won't be around for much longer. You need to save the Shaderlords and defeat Le Monsieur so that we can regain our forms!"
    wire2 "You can do this Molina!" 
    "The weird wireframes disappear"
    mateo "Uhhhhh what just happened?"
    mateo "Whelp."
    mateo "I guess I have to save these shaderlords now."
    mateo "Shmerp."
    mateo "If I'm gonna defeat this Le Moose guy-"
    "It's Le Monsieur."
    mateo "Whatever. If I'm gonna defeat him....I need coffee."
    mateo "COFFFFEEEEEEEEEEEEE!!!"
    stop music fadeout 3.0
    play music "lib.wav" fadein 8.0
    scene bglib with fade
    "You make your way up to the Library Cafe. If you had only checked your mip_map before rushing there, you would know that there was far more in store for you than just an Iced Cafe Latte with hazelnut syrup."
    mateo "What? Okay whatever, I’ll check the mip_map later, right now I just want coffee."
    "You enter the Library Cafe, still unaware of what you’re walking into."
    show aliahappy at left
    alia "Mateo! Finally!"
    mateo "Wait, you know me?"
    hide aliahappy
    show alescared at right
    ale "Of course we do! And we’ve been waiting for you for a long time! We’re trapped in bad Open Frameworks code, and you need to free us!"
    hide alescared
    show aliahappy at left
    alia "Yes! Only with our powers combined can Le Monsieur be defeated!"
    mateo "And, what are these powers?"
    hide aliahappy
    show alescared at right
    ale "We control graphics that lie outside of photorealism. We breathe the Breath of the Wild. We control…CELL SHADERS!"
    "..."
    hide alescared
    mateo "Floop."
    mateo "I mean.."
    mateo "I'll try to free you."
    mateo "I guess."
    "The Shaderlords are trapped in an ofGLPrison(). What do you do?"
    menu:
        "Check the Open Frameworks Documentation.":
            jump open
        "Mash buttons blindly.":
            jump buttonmash

label open:
    "You try to look up this particular Open Frameworks method, but there’s no good documentation online!"
    menu:
        "Mash Buttons Blindly.":
            jump buttonmash
            
label buttonmash:
    mateo "Urgh! Not again, I guess I'm gonna have to wing it."
    "*Mashes buttons blindly*"
    "Amazingly....it works."
    "In a flurry of keystrokes, with the power of Open Frameworks, you quickly resolve the Segmentation Fault that was keeping the Cell Lords trapped."
    show alescared at right
    ale "Free at last! we’re going to defeat Le Monsieur, we need more than just Cell Shaders. If only we knew where the other Shaderlords were trapped, we could free them all!"
    mateo "I mean, I met these two weird Meshes, and they gave me a mip_map with all the Shaderlords’ locations. The closest ones to us are the Phong shaders in the Baraha."
    hide alescared 
    show aliahappy at left
    alia "Yalla! Or, as Google Translate tells me they say in Spanish, “estas usando este software de traducción de forma incorrecta. por favor, consulta el manual.”"
    hide aliascared
    show alescared at right
    ale "That’s not...okay, nevermind. We have a sassy overlord to defeat!"
    stop music fadeout 3.0
    "You enter the Living Room.
     Two people there seem to be playing a game on the projector screen.
     At least, they’re trying to.."
    scene bgLivingRoom with fade
    play music "livingroom.mp3" fadein 3.0
    show gracescared at left
    grace "God dammit where is the last clue!!"
    hide gracescared
    mateo "(Heh she just lost the game)"
    show harshiniscared at right
    harshini "We've been here for hours"
    hide harshiniscared
    "They appear to be trying to solve a room escape puzzle of a very familiar cabin, albeit without any colors."
    show shenukareg at right
    shenuka "Why can’t you just leave?"
    hide shenukareg 
    show gracescared at left
    grace "We would but Le Monsieur has fitted us both with these bracelets that will inject us with Soparil if we leave without solving this puzzle."
    "You see that they have metal bracelets firmly attached to their left wrists."
    hide gracescared
    mateo "THAT MOTHERFUCKER!!!"
    show harshiniscared at right
    harshini "Mateo! Please help us! We've looked everywhere!"
    harshini "WE HAVE ONLY ONE MORE ATTEMPT LEFTTTTTTT!!!"
    hide harshiniscared 
    show gracescared at left
    grace "We just need one more note, then we can crack the suitcase combination…"
    hide gracescared 
    "Where do you look?"
    menu:
        "Behind the mirror":
            jump mirror
        "In the sink":
            jump sink
        "Under the pillow":
            jump pillow
        "Screw it, the code is 7485":
            jump code

label mirror:
    "There's nothing here!"
    mateo "PUTA MADRE!"
    "Where do you look next?"
    menu:
        "In the sink":
            jump sink
        "Under the pillow":
            jump pillow
        "Screw it, the code is 7485":
            jump code
label sink:
    "There's nothing here!"
    "...."
    mateo "PUTA MADREEE!!"
    "Where do you look next?"
    menu:
        "Behind the mirror":
            jump pillow
        "Under the pillow":
            jump pillow
        "Screw it, the code is 7485":
            jump code
label pillow:
    show harshinihappy at right
    harshini "There it is!"
    hide harshinihappy
    show gracehappy at left
    grace "So the code was 7485"
    hide gracehappy 
    "Input code?"
    menu:
        "Yes":
            jump code
label code:
    show harshinihappy at right
    harshini "Well...that was quick."
    hide harshinihappy
    "With a loud clink, the bracelets fall to the floor."
    show harshinihappy
    harshini "Yes!! We can finally leave now!"
    hide harshinihappy
    "With the six Shaderlords by your side, you feel confident in your ability to take on Le Monsieur."
    mateo "Frens, I feel confident in our ability to take on Le Monsieur!"
    show harshinihappy at right
    show gracehappy at left
    "Precisely."
    hide gracehappy
    harshini "Wait! We have no hope of defeating them without them!"
    hide harshinihappy
    show shenukareg
    shenuka "Dammit. I think I know who you mean."
    hide shenukareg
    mateo "(Heh. She just lost the game)"
    mateo "(Wait. So did I)"
    mateo "(Fuck.)"
    "...."
    "Dammet."
    stop music fadeout 3.0
    "There’s two graphics-lords who the Shaderlord could not trap, so instead he simply kept them distracted while he hatched his evil plan. They are Norm and Mal, keepers of normal mapping. They’re in the Arts Center, let’s go!"
    "You and your odd adventuring party make your way to the Arts Center. You feel an uneasy presence lingering in the air. The smell of cigarette smoke and dry, politically charged sarcasm fills your lungs. Le Monsieur is close. You can feel it."
    "But, for now, you cautiously tip toe into the Howler Radio room."
    play music "howler.mp3" fadein 3.0
    scene bghowler with fade
    show abdullahreg at right
    show shantanureg at left
    norm "Salutations."
    mal "Yooooooo!"
    hide abdullahreg
    hide shantanureg
    mateo "Wait, are you Norm or Mal?"
    show abdullahreg at right
    show shantanureg at left
    mal "Yes."
    norm "Yep."
    hide abdullahreg
    hide shantanureg
    mateo "No, but which one are you?"
    show abdullahreg at right
    show shantanureg at left
    norm "Beats me haha. One of them, for sure. Hard to say. But, we are Norm and Mal."
    norm "And, we have a bit of a situation on our hands."
    hide abdullahreg
    hide shantanureg
    show gracescared
    grace "They've been here trying to break the chains of this linked list for ages."
    hide gracescared
    mateo "Haven't you broken it yet?"
    show abdullahreg at right
    show shantanureg at left
    norm "We would have, but there is a slight issue."
    mal "The code's in French."
    hide abdullahreg
    hide shantanureg
    mateo "wooOOOOwww guys"
    menu:
        "Rip the head of the list off":
            jump head
        "Stare them in the eyes and say 'Dammet'":
            jump dammet
label head:
    "The head gets ripped off."
    "The nodes go haywire!"
    "The links shatter."
    mateo "Pfft you fucking pompous CS majors and your bullshit.."
    mateo "Always making life complicated with your stupid code.."
    jump continuegame

label dammet:
    show abdullahreg at right
    show shantanureg at left
    mateo "DAMMET"
    norm "DAMMIT!"
    mal "DAMMIT!"
    jump head

label continuegame:
    "This breaks them out of the linked list."
    show abdullahreg at right
    show shantanureg at left
    norm "AHHHHHHHHHHHHH DANGLING POINTERS EVERYWHERE!!!!!!!"
    mal "Calm the fuck down!"
    norm "I CANT STAND IT ANYMORE. BAD REFERENCES EVERYWHEREEEEEEEEEE!!"
    hide abdullahreg
    hide shantanureg
    mateo "You guys are impossible. Let's go get rid of Le Monsieur so that I can go back to sleep please?"
    show abdullahreg at right
    show shantanureg at left
    mal "Excellent choice!"
    norm "Bleh."
    norm "Sure thing!"
    hide abdullahreg
    hide shantanureg
    stop music 
    ukn "Huehuehuehue."
    scene bgIMClass with fade
    "An evil snicker reverberates from the surroundings."
    mateo "Huh?"
    "A strange rabbit looking creature emerges from the surroundings."
    mateo "Uhhh who the fuck are you?"
    show rabbit
    play music "battle.mp3" fadein 2.0
    bunny "Show some respect to me, you peasant! I’m the Evil Overlord (2.0) Monsieur D3P4Z and this is my domain!"
    hide rabbit
    mateo "WHAT?! WHAT THE FUCK?!"
    show rabbit
    d3p4z "Indeed, c’est vrai! You weren’t able to make it as an engineer, and now, you won’t make it out of here alive!"
    hide rabbit
    show gracescared
    grace "Not if we've got anything to say about it - literally! It's time for a sass-off D3P4Z!"
    hide gracescared
    mateo "No. Frens, this is something I have to do alone."
    "You crack your knuckles and stare the evil French rabbit in the eyes."
    mateo "PUTA MADRE, COME AT ME YOU STUPID LITTLE PIECE OF USELESS SHIT!"
    show rabbit2
    d3p4z "Let's dansons, motherfucker!"
    "It's Sass Off Time!"
    hide rabbit2
    mateo "*pulls out an rusty pistol with a flaming fox engraved on its barrell*"
    show rabbit2
    d3p4z "Ha! Look at that pathetic thing! You can’t keep up with this!"
    hide rabbit2
    "He pulls put a bag of coffee beans and a canon with an infinity symbol on it"
    show rabbit2
    d3p4z "You can’t think of competing with this! The Infinity Canon powered by the finest beans from a lone Indonesian island will overpower your one-trick wonder!"
    d3p4z "Try me you stupid piece of fuck! Fire!"
    hide rabbit2
    "The pistol fires, but a wall of fire encloses D3P4Z, destroying the attack!"
    show rabbit2
    d3p4z "Ha! Pathetic! It's my turn now!"
    hide rabbit2
    "The canon launches, but the beans just scatter all over the place."
    show rabbit2
    d3p4z "STUPID PIECE OF FUCK! WHAT'S WRONG WITH YOU?!"
    hide rabbit2
    mateo "AHAHAHAHHAHAHHAHAHAHAHAHHAHA!"
    mateo "YOU FORGOT TO TRIM THE BEANS BEFORE SENDING THEM ACROSS THE CANON'S SERIAL LAUNCHER YOU FOOL!"
    mateo "ALL THAT EXTRA SPACE JUST CAUSED A MASSIVE CLUSTERFUCK IN YOUR CANON!"
    show rabbit2
    d3p4z "GOD! WHY ISN'T THIS STUPID THING WORKING?! THE MACHINE TAKES VIRTUALLY FOREVER TO RECHARGE!"
    hide rabbit2
    mateo "(This is my only chance, he's gonna be occupied for the next few seconds while the canon reloads)"
    "Mateo pulls out a weird blue sapphire out of his pocket."
    mateo "(This will take him out in a single strike)."
    mateo "(But...)"
    mateo "(I'll have to place this on the rails and use the pistol in unsafe mode..)"
    mateo "*Gulp*"
    mateo "(Now's not the time to PANIC!)"
    mateo "(It looks like I have no choice..)"
    mateo "(Here goes nothing..)"
    "Mateo loads the ruby and flips the safety switch on the pistol."
    mateo "TO BERLIN AND BEYOND YOU STUPID PIECE OF FUCK!"
    "A blinding flash envelopes the surroundings."
    show rabbit2
    stop music
    d3p4z "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!!"
    hide rabbit2
    "After the flash subsides, color gradually returns to the world, and everything is illuminated once again."
    play music "ending.mp3" fadein 1.0
    scene bgIMClassColor with dissolve
    everyone "Yes! You did it!"
    mateo "YEEEEEEEE!"
    "You hear the sound of footsteps and you hear a familiar voice."
    show mingreg
    ming "MOLINAAAAAAAAAAAAAAAAAAAAAA"
    ming "You did it!"
    hide mingreg
    mateo "Wow Ming you did the appear thing!"
    "You hear more footsteps and another familiar voice."
    show thirangiereg
    thirangie "I'm here toooooooo."
    hide thirangiereg
    mateo "Hmm...not too bad, you're earlier than expected, I am proud."
    show thirangiereg
    thirangie "Hey, its not easy roaming around without any form y'know."
    hide thirangiereg
    mateo "Floop"
    show thirangiereg
    thirangie "Looks like you've had quite an adventure"
    hide thirangiereg
    mateo "I guess"
    show thirangiereg
    thirangie "Well, we wouldn't be here right now unless you beat D3P4Z so I guess we owe you our thanks ^_^"
    hide thirangiereg
    show mingreg
    ming "Yeah, you showed that Frenchie the power of Molina!"
    hide mingreg
    show shantanureg
    norm "Ayyy!"
    hide shantanureg
    mateo "..."
    mateo "(Fuck, it's been 30 minutes already.)"
    mateo "DAMMET!"
    everyone "DAMMET!!"
    "And that's how everyone lost the game. Again."
    stop music fadeout 3.0
    "The End."
    

    return
