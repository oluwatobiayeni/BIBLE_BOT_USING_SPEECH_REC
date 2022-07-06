import speech_recognition as sr
import pyttsx3
import pywhatkit
import gtts
from playsound import playsound
import os
import glob


listener = sr. Recognizer()
#to adjust microphone sensitivity
listener.energy_threshold = 4000
listener.dynamic_energy_threshold = False
engine = pyttsx3.init()
def talk(text,id):
    if id == 15:
        print("repeat yourself")
    tts = gtts.gTTS(text)
    tts.save(f"./oro/hello{str(id)}.mp3")
    playsound(f"./oro/hello{str(id)}.mp3")
    
def take_command():
    try:
        print("entered.df")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            playsound("listening.mp3")
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Daniel" in command:
                command = command.replace("bibot","")
                print(command)
        print("entered")
        return(command)
    except Exception as e:
        print(e)
        pass
    

def Run_Troy(globalConvo):
    command = take_command()
    globalConvo.append("User: "+command)
    print(command)
    if "hey" in command or "hello" in command:
        talk("Hi! I’m bibot, a bible bot designed to cater to your biblical needs.\n How can I help you today?",1)
        globalConvo.append("Bi-Bot :"+"Hi! I’m bibot, a bible bot designed to cater to your biblical needs.\n How can I help you today?")
        print("Hi! I’m Bi-Bot, a bible bot designed to cater to your biblical needs.\n How can I help you today?")
   

    elif "" + "bible study" in command:
        talk("yay! That’s so exciting to know.\n What would you like to study about today?",2)
        globalConvo.append("Bi-Bot :"+"yay! That’s so exciting to know.\n What would you like to study about today?")
        print("YAY!!! That’s so exciting to know.\n What would you like to study about today?")
#keyword for anger
    elif "" + "anger" in command:
        talk("Okay!! I’ll display scriptures in relation to anger right away.\n"
             "Psalms 86:15  But you, O Lord, are a God merciful and gracious, slow to anger and abounding in steadfast love and faithfulness.\n"
             "Proverbs 14:29  Whoever is slow to anger has great understanding, but he who has a hasty temper exalts folly.\n"
             "Proverbs 15:1  A soft answer turns away wrath, but a harsh word stirs up anger.",3)
        globalConvo.append("Bi-Bot :"+"Okay!! I’ll display scriptures in relation to anger right away.\n"
              "Psalms 86:15  But you, O Lord, are a God merciful and gracious, slow to anger and abounding in steadfast love and faithfulness.\n"
              "Proverbs 14:29  Whoever is slow to anger has great understanding, but he who has a hasty temper exalts folly.\n"
              "Proverbs 15:1  A soft answer turns away wrath, but a harsh word stirs up anger.")      
        print("Okay!! I’ll display scriptures in relation to anger right away.\n"
              "Psalms 86:15  But you, O Lord, are a God merciful and gracious, slow to anger and abounding in steadfast love and faithfulness.\n"
              "Proverbs 14:29  Whoever is slow to anger has great understanding, but he who has a hasty temper exalts folly.\n"
              "Proverbs 15:1  A soft answer turns away wrath, but a harsh word stirs up anger.",)
#keyword for love
    elif "" + "love" in command:
        talk("Okay!! I’ll display scriptures in relation to love right away.\n"
             "Romans5:8  But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us.\n"
             "Ephesians 1:4  According as he hath chosen us in him before the foundation of the world, that we should be holy and without blame before him in love.\n"
             "1 john4:9  In this was manifested the love of God toward us, because that God sent his only begotten Son into the world, that we might live through him.\n"
             "Psalms 143:8  Let the morning bring me word of your unfailing love, for I have put my trust in you. Show me the way I should go, for to you I entrust my life.\n"
             " 1 John 4:16: And so we know and rely on the love God has for us. God is love.",4)
        globalConvo.append("Bi-Bot :"+"Okay!! I’ll display scriptures in relation to love right away.\n"
              "Romans5:8  But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us.\n"
              "Ephesians 1:4  According as he hath chosen us in him before the foundation of the world, that we should be holy and without blame before him in love.\n"
              "1 john4:9  In this was manifested the love of God toward us, because that God sent his only begotten Son into the world, that we might live through him.\n"
              "Psalms 143:8  Let the morning bring me word of your unfailing love, for I have put my trust in you. Show me the way I should go, for to you I entrust my life.\n"
              " 1 John 4:16: And so we know and rely on the love God has for us. God is love.")
        print("Okay!! I’ll display scriptures in relation to love right away.\n"
              "Romans5:8  But God commendeth his love toward us, in that, while we were yet sinners, Christ died for us.\n"
              "Ephesians 1:4  According as he hath chosen us in him before the foundation of the world, that we should be holy and without blame before him in love.\n"
              "1 john4:9  In this was manifested the love of God toward us, because that God sent his only begotten Son into the world, that we might live through him.\n"
              "Psalms 143:8  Let the morning bring me word of your unfailing love, for I have put my trust in you. Show me the way I should go, for to you I entrust my life.\n"
              " 1 John 4:16: And so we know and rely on the love God has for us. God is love.")
#keyword for abandoned
    elif "" + "abandoned" in command:
        talk("Okay!! I’ll display scriptures in relation to abandoned right away.\n"
            "Isaiah 41:10  so do not fear for I am with you, Do not be dismayed, for I am your God, I will strengthen you and help you; I will uphold you with my righteous right hand.\n"
            "Psalm 34:18  The lord is close to the brokenhearted and saves those who are crushed in spirit.\n"
            "Deuteronomy 31:6 Be strong and courageous. For the lord your God goes with you; he will never leave you nor forsake you.", 5)
        globalConvo.append("Bi-Bot :"+ "Isaiah 41:10  so do not fear for I am with you, Do not be dismayed, for I am your God, I will strengthen you and help you; I will uphold you with my righteous right hand.\n"
            "Psalm 34:18  The lord is close to the brokenhearted and saves those who are crushed in spirit.\n"
            "Deuteronomy 31:6 Be strong and courageous. For the lord your God goes with you; he will never leave you nor forsake you.")
        print(
            "Isaiah 41:10  so do not fear for I am with you, Do not be dismayed, for I am your God, I will strengthen you and help you; I will uphold you with my righteous right hand.\n"
            "Psalm 34:18  The lord is close to the brokenhearted and saves those who are crushed in spirit.\n"
            "Deuteronomy 31:6 Be strong and courageous. For the lord your God goes with you; he will never leave you nor forsake you.")
#keyword for fear
    elif ""+"fear" in command:
        talk("Okay!! I’ll display scriptures in relation to fear right away\n"
             "Psalm 34:4-3 I sought the Lord, and he answered me and delivered me from all my fears. Those who look to him are radiant, and their faces shall never be ashamed.\n"
             "Psalm 23:4 Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n"
             "Psalm27:1 The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?\n",6 )
        globalConvo.append("Bi-Bot :"+ "Okay!! I’ll display scriptures in relation to fear right away.\n"
              "Psalm 34:4-3 I sought the Lord, and he answered me and delivered me from all my fears. Those who look to him are radiant, and their faces shall never be ashamed.\n"
              "Psalm 23:4 Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n"
              "Psalm27:1 The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?\n" )
        print("Okay!! I’ll display scriptures in relation to fear right away.\n"
              "Psalm 34:4-3 I sought the Lord, and he answered me and delivered me from all my fears. Those who look to him are radiant, and their faces shall never be ashamed.\n"
              "Psalm 23:4 Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n"
              "Psalm27:1 The Lord is my light and my salvation; whom shall I fear? The Lord is the stronghold of my life; of whom shall I be afraid?\n" )
#keyword for anxiety
    elif ""+"anxiety" in command:
        talk("okay!! I'll display scriptures in relation to fear right away\n"
            "Phillipians4:6 Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God\n And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.\n"
            "proverbs12:25 Anxiety weighs down the heart, but a kind word cheers it up.\n"
            "psalms23:4 Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n")
        globalConvo.append("Bi-Bot:"+"okay!! I'll display scriptures in relation to fear right away\n"
            "Phillipians4:6 Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God\n And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.\n"
            "proverbs12:25 Anxiety weighs down the heart, but a kind word cheers it up.\n"
            "psalms23:4 Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n")
        print("okay!! I'll display scriptures in relation to fear right away\n"
            "Phillipians4:6 Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God\n And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.\n"
            "proverbs12:25 Anxiety weighs down the heart, but a kind word cheers it up.\n"
            "psalms23:4 Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.\n")    
    elif "thank you very much " in command or "thank you" in command:
        talk(
            "You’re welcome!!\n Would you also like me to recommend books to help solidify your knowledge on the topic?",7)
        globalConvo.append("Bi-Bot :"+"You’re welcome!!\n Would you also like me to recommend books to help solidify your knowledge on the topic?")
        print(
            "You’re welcome!!\n Would you also like me to recommend books to help solidify your knowledge on the topic?")

    elif "no" in command or "that will be all for now" in command:
        talk("Alright! Look forward to seeing you soon again.",8)
        globalConvo.append("Bi-Bot :"+"Alright! Look forward to seeing you soon again.")
        print("Alright! Look forward to seeing you soon again.")
        return "end"
    elif "yes" in command:
        book_rec(globalConvo)

#play songs and videos from youtube
    elif "play" in command:
        song = command.replace("play", "")
        talk("playing" + song, 34)
        pywhatkit.playonyt(song)
    else:
        talk("please repeat yourself", 15)

# while True:
#    Run_Troy()

def manual():
    conversation_length = 8
    gbese=0
    globalHistory = []
    while conversation_length != 0 or gbese!="end":
    # while gbese=="end":
        try:
            files = glob.glob('./oro/*') 
            for f in files: 
                os.remove(f)
            print("conversation_length is remaining ", conversation_length)
            gbese=Run_Troy(globalHistory)
            conversation_length -=1
            if gbese=='end':
                conversation_length=0
        except Exception as e:
            print(e,'gbese re o')

    return globalHistory
# take_command()

def book_rec(globalConvo):
    talk('Which book do you want',404)
    globalConvo.append("Bi-Bot :"+"Which book do you want")
    print("which book do you want")
    book=take_command()
    print(book)
#books reommendation for anger
    if ""+"anger" in book:
     talk("Anger: Escaping the maze by David Powlison.\n "
             "Controlling Anger: Responding constructively when life goes wrong by David Powlison.\n"
             " Anger, anxiety and fear: a biblical perspective by stuart scott.  ", 10)
     globalConvo.append("Bi-Bot :"+"Anger: Escaping the maze by David Powlison.\n "
              "Controlling Anger: Responding constructively when life goes wrong by David Powlison.\n"
              " Anger, anxiety and fear: a biblical perspective by stuart scott.")
     print("Anger: Escaping the maze by David Powlison.\n "
              "Controlling Anger: Responding constructively when life goes wrong by David Powlison.\n"
              " Anger, anxiety and fear: a biblical perspective by stuart scott.")
#books recommendation for love
    elif ""+"love" in book:
        talk("Bring on the blessings by Beverly Jenkins.\n "
             "Isle of hope by Julie Lessman,\n "
             "The preachers promise by Piper Hugley.",9)
        globalConvo.append("Bi-Bot :"+"Bring on the blessings by Beverly Jenkins.\n"
              "Isle of hope by Julie Lessman.\n"
              "The preachers promise by Piper Hugley.")
        print("Bring on the blessings by Beverly Jenkins.\n"
              "Isle of hope by Julie Lessman.\n"
              "The preachers promise by Piper Hugley.")
#books reommendation for abandonment
    elif ""+"abandonment" in book:
        talk("The Journey from Abandonment to Healing by Susan Anderson.\n ",9)
        globalConvo.append("Bi-Bot :"+"The Journey from Abandonment to Healing by Susan Anderson.\n")
        print("The Journey from Abandonment to Healing by Susan Anderson.\n")
    elif ""+"fear" in book:
        talk("How to stop worrying and start living by Dale Carnegie.\n"
        "Fear of failure by James Scott\n"
        "Speak with no fear by Mike Acker.",9)
        globalConvo.append("How to stop worrying and start living by Dale Carnegie.\n"
        "Fear of failure by James Scott\n"
        "Speak with no fear by Mike Acker.")
        print("How to stop worrying and start living by Dale Carnegie.\n"
        "Fear of failure by James Scott\n"
        "Speak with no fear by Mike Acker.")
    elif ""+"anxiety" in book:
        talk("A Liberated mind by Steven C.Hayes.\n"
        "Be calm by Jill P Weber",9)
        globalConvo.append("A Liberated mind by Steven C.Hayes.\n"
        "Be calm by Jill P Weber")
        print("A Liberated mind by Steven C.Hayes.\n"
        "Be calm by Jill P Weber")

            


