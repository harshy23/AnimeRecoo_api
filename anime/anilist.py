import requests

ANILIST_API_URL = "https://graphql.anilist.co"

def anilist_request(query,variables):
    response = requests.post(
        ANILIST_API_URL,
        json = {"query":query,"variables":variables},
        headers = {'Content-Type': 'application/json','Accept': 'application/json'}
    )

    return response.json()

def anime_by_genre(genre):
    query = '''
        query ($genre:String){
        Page(perPage:4){
          media (genre_in: [$genre], type: ANIME) { 
            id
            title {
              romaji
              english
            }
            genres
            popularity
          }
        }
    }
'''
    variables ={"genre" : genre}
    return anilist_request(query,variables)

def anime_by_name(name):
    query = '''
        query ($name:String){
        Page(perPage:4){
          media (search: $name, type: ANIME){ 
            id
            title {
              romaji
              english
            }
            genres
            popularity
          }
        }
    }
'''
    variables ={"name" : name}
    return anilist_request(query,variables)

def anime_by_recommendations(genres):
    query = '''
        query ($list_genres:[String]){
         Page(perPage:4){
          media (genre_in: $list_genres, type: ANIME){ 
            id
            title {
              romaji
              english
            }
            genres
            description
            episodes
            popularity
          }
        }
    }
'''
    variables ={"list_genres" : genres}
    return anilist_request(query,variables)
