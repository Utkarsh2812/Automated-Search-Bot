import webbrowser
import random
import string

# define the list of search queries
queries = []

# generate 5 random queries and add them to the list
for i in range(5):
    query = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    queries.append(query)

# loop through the queries and open a new tab for each one
for query in queries:
    search_url = 'https://www.bing.com/search?q=' + query
    webbrowser.open_new_tab(search_url)
