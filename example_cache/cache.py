import requests
import time

def cache(func: callable) -> callable:
    #TODO implement a caching mechanism when hitting the Github profiles API


@cache
def get_github_profile(profile_id: str) -> dict:
    
    response = requests.get(f'https://api.github.com/users/{profile_id}', timeout=10)

    response.raise_for_status()

    return response.json()

get_github_profile("mourtisma")
get_github_profile("ismailmourtada")
get_github_profile("mourtisma")
