import requests


def send_request(urlweb):
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': '0E4PM0ERBHIVC9O4NWLGPE91J3DBWBOVBAJXX4RY4PS5SWGG0WZ3C6ORM1BIAPJ6UDKU1WWTQGLSHB1Z',
            'url': urlweb,
            'wait': '1000',
            'block_ads': 'True',
            'render_js': 'False'
        },

    )
    # print('Response HTTP Status Code: ', response.status_code)
    # print('Response HTTP Response Body: ', response.content)

    return response
