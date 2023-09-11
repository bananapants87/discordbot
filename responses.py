import random, requests, discord, bot, math, apis

#words to add into filter
bannedWords = ["fuck", "shit", "bitch"]

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == "hello":
        return 'Hey there!'
    
    if p_message == "!roll":
        return str(random.randint(1,6))
    
    if p_message == "!help":
        return "`This is a help message that i cant be bothered to modify now.\n actually, the commands available are !dictionary <word>, !synonym <word>, !roll, !ping`"
    
    if p_message == "!ping": #test bot latency
        print(f"Pong! {(bot.client.latency * 1000)}ms")
        return f"Pong! {math.ceil(bot.client.latency * 1000)}ms"
    
    if p_message in bannedWords: #basic filter without action
        return f"Hey! You're not allowed to say that here."
    
    
def dictionary(message):
    user_message = message[12:]
    dictionary_api = apis.getAPI("FD", user_message)
    r = requests.get(dictionary_api)
    res = r.json()
    definitionString = f"Definitions for {user_message}:"
                
    for i in range(len(res[0]["meanings"])):
        definitionString += f"\n\nPart of Speech: **{res[0]['meanings'][i]['partOfSpeech']}**\n"
        counter = 1
        for j in res[0]["meanings"][i]["definitions"]:
            if "definition" in j:
                definitionString += f"\n**Definition {counter}**: {j['definition']}"
                counter+=1
                
    return definitionString
    
def synonym(message):
    user_message = message[9:]
    thesaurus_api = apis.getAPI("MW", user_message)
    r = requests.get(thesaurus_api)
    res = r.json()
    synonymString = f"Synonyms for {user_message}:"
    for i in res[0]["meta"]["syns"]:
        for j in i:
            synonymString += f"\n{j}"
                    
    return(synonymString)

def synonymOffensive(message):
    user_message = message[9:]
    thesaurus_api = apis.getAPI("MW", user_message)
    r = requests.get(thesaurus_api)
    res = r.json()
    synonymString = f"Synonyms for {user_message}:"
    for i in res:
            synonymString += f"\n{i}"
                    
    return(synonymString)