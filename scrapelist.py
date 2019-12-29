import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

import util

URL_BASE = 'https://losangeles.craigslist.org/search/mcy?s='
URL_SUFFIX = '&hasPic=1&min_price=800&max_price=2500'
BIG_FILE = 'posts.json'
POSTS_PER_PAGE = 120


def add_new_posts(posts_df, posts_new):
    def get_post_id(post):
        return post['data-pid']

    def get_post_title(post):
        return post.find(name='a', attrs={'class': 'result-title hdrlnk'}).text

    def get_post_price(post):
        return post.find(name='span', attrs={'class': 'result-price'}).text[1:]

    def get_post_date(post):
        return post.find(name='time', attrs={'class': 'result-date'})['datetime']

    def filter_out_post_by_title(title):
        result = False
        if 'scooter' in title.lower():
            result = True

        return result

    for post in posts_new:
        title = get_post_title(post)
        post_id = get_post_id(post)
        date = get_post_date(post)
        price = get_post_price(post)

        if filter_out_post_by_title(title):            
            continue

        if title not in posts_df['title'].values:
            series_new = pd.Series({'title': title,
                                    'id': [post_id],
                                    'date': [date],
                                    'price': [price]})
            posts_df = posts_df.append(series_new, ignore_index=True)
        else:
            index = np.where(posts_df['title'] == title)[0][0]
            posts_df.loc[index, 'id'].append(post_id)
            posts_df.loc[index, 'date'].append(date)
            posts_df.loc[index, 'price'].append(price)

    return posts_df


def main():
    posts = util.load_json_to_dataframe(BIG_FILE)

    post_to_start_with = 0
    while True:
        req = requests.get(URL_BASE + str(post_to_start_with) + URL_SUFFIX)
        soup = BeautifulSoup(req.text, 'html.parser')
        posts_new = soup.find_all(attrs={'class': 'result-row'})
        if len(posts_new) == 0:
            break
        posts = add_new_posts(posts, posts_new)
        post_to_start_with += POSTS_PER_PAGE
    
    posts.to_json(BIG_FILE)


if __name__ == "__main__":
    thing = main()
