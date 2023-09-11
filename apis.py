import keyring
def getAPI(apitype, user_message):
    if apitype == 'MW':
        token = keyring.get_password("MWThesaurus", "username")
        MWThesaurusAPILink = f"https://dictionaryapi.com/api/v3/references/thesaurus/json/{user_message}?key={token}"
        return MWThesaurusAPILink
    elif apitype == 'FD': 
        FreeDictionaryAPI = f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_message}"
        return FreeDictionaryAPI