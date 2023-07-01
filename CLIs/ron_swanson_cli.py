import requests
import typer
import os
from typing import List


def clear():
    os.system('clear')

def ron_swanson_quote(query: List[str] = typer.Argument(None, help="Enter one or more search terms. If nothing entered, API will return a random quote")):
    """A generic function that retrieves one or more (or none) Ron Swanson quotes
    using a search term ('query'). If 'query' is an empty string, the api will
    return a random quote. Requires calling program to import requests module. 
    Return value is a list. It is left to the calling code to decide 
    what to do with the return value. Alternatively, user could comment out 
    'return response.json()' and uncomment the three following lines to print the
    quote(s) from the function"""
    search = " ".join(query)
    endpoint = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/search/{}".format(
        search)

    response = requests.get(endpoint)
    results = response.json()
    clear()
    print()
    for quote in results:
        print(quote)
        print()


if __name__ == '__main__':
    typer.run(ron_swanson_quote)


