import csv
import requests
import time

# GitHub authentication
TOKEN = 'xxx' # Your GitHub Token
HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Parameters
CITY_VARIATIONS = ["Moscow"]
FOLLOWER_THRESHOLD = 50
BASE_URL = 'https://api.github.com'


def clean_company_name(company):
    if company:
        company = company.strip().lstrip('@').upper()
    return company or ''


def search_users(city_list, followers_min):
    users = []
    for city in city_list:
        page = 1
        while True:
            query = f'location:{city}'
            response = requests.get(f'{BASE_URL}/search/users', headers=HEADERS, params={'q': query, 'page': page, 'per_page': 30})
            data = response.json()
            print(f"Search API Response for {city} (Page {page}): {data}")  
            if 'items' not in data:
                print(f"Error: 'items' not found in response. Full response: {data}")
                break
            for user in data['items']:
                user_detail_response = requests.get(f"{BASE_URL}/users/{user['login']}", headers=HEADERS)
                user_detail = user_detail_response.json()
                if user_detail.get('followers', 0) > followers_min:
                    users.append(user_detail)
                    print(f"Added User: {user_detail['login']}")
            if len(data['items']) < 30:
                break
            page += 1
            time.sleep(2)
    return users


def write_users_csv(users):
    with open('users.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'login', 'name', 'company', 'location', 'email', 'hireable', 'bio',
            'public_repos', 'followers', 'following', 'created_at'
        ])
        for user in users:
            writer.writerow([
                user['login'],
                user.get('name', ''),
                clean_company_name(user.get('company', '')),
                user.get('location', ''),
                user.get('email', ''),
                str(user.get('hireable', '')).lower(),
                user.get('bio', ''),
                user.get('public_repos', ''),
                user.get('followers', ''),
                user.get('following', ''),
                user.get('created_at', '')
            ])
            print(f"Wrote User to CSV: {user['login']}")


if __name__ == "__main__":
    moscow_users = search_users(CITY_VARIATIONS, FOLLOWER_THRESHOLD)
    write_users_csv(moscow_users)
    print("CSV file 'users.csv' has been created successfully.")
