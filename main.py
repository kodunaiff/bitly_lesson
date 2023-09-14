import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'long_url': link,
    }
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json().get('id')


def count_clicks(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}',
    }
    params = {
        'unit': 'day',
        'units': '-1',
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_bitlink(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Получает короткую ссылку или количество кликов'
    )
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    token = os.environ['BITLY_TOKEN']

    try:
        parsed_url = urlparse(args.link)
        bitlink = f'{parsed_url.netloc}{parsed_url.path}'
        if is_bitlink(token, bitlink):
            print('По вашей ссылке прошли:',
                  count_clicks(token, bitlink), 'раз(а)')

        else:
            print('Битлинк', shorten_link(token, args.link))
    except requests.exceptions.HTTPError as errh:
        print(f'HTTP Error: {errh}')


if __name__ == "__main__":
    main()
