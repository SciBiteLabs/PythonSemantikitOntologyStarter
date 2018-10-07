import json, requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

semantikit_server = "http://ugm.scibite.com:8090/api/Synonym%20suggestions/1.0/suggest_synonyms"


def get_similar_word(word, limit="10", sources="MedLine_Phrased,MedLine_Basic"):
    '''
    The get similar word function to return semantically related phrases to a given query phrase.
    :param word: query word(s) to get related words for
    :param limit: limit number of results
    :param sources: comma separated list of source name to find semantically related words from
    :return: dictionary of results
    '''
    try:
        print(word)
        parameters = {"query": word.lower(), "limit": limit, "sources": sources}
        j = json.loads(requests.get(semantikit_server, verify=False, params=parameters).text)

        if j['results']:
            return j
        else:
            print('no results')
    except:
        print('error trying to find similar words for ' + word)