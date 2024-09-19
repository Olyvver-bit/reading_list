import requests
from bs4 import BeautifulSoup
import pandas as pd


def book_list(url):
    try: 
        response = requests.get(url)

        if response.status_code != 200: 
            print(f"Failed to get the webpage: {response.status_code}")
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        lib500 = soup.find_all('table', id = 'lib500list')

        headers = [soup.find_all('th')]
        
        # Python Pandas Dataframe is used to store the list of 500 books titles and author names in a tabular format
        df = pd.DataFrame(columns = headers)
        rows = soup.find_all('tr')
        for i in rows[1:]:
            data = i.find_all('td')
            row = [tr.text for tr in data]
            length = len(df)
            df.loc[length] = row

        df = df.iloc[:, 1:]
        rec_list = df.sample(5) # Pandas Dataframe Sample is used to pick out a random list of 5 books from The Complete 500 book list from OCLC

        return rec_list
    
    except Exception as e: 
        print(f"An error has occured: {e}")
        return None
        

# This is the main part of the program
url = "https://www.oclc.org/en/worldcat/library100/top500.html"
print('Monthly Reading List')
print(book_list(url))
