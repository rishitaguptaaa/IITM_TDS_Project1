import csv
import requests
import time

# GitHub authentication
TOKEN = 'xxxx' # Your GitHub Token
HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}
BASE_URL = 'https://api.github.com'


def get_user_repos(username):
    repos = []
    page = 1
    while page <= 17:  
        response = requests.get(f'{BASE_URL}/users/{username}/repos', headers=HEADERS, params={'page': page, 'per_page': 30})
        data = response.json()
        print(f"Repositories API Response for {username} (Page {page}): {data}")  
        if isinstance(data, list): 
            repos.extend(data)
        else:
            print(f"Error fetching repositories for {username}: {data}")
            break  
        if len(data) < 30:
            break
        page += 1
        time.sleep(1)      
    return repos


def write_repositories_csv(usernames):
    with open('repositories (3).csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count',
            'language', 'has_projects', 'has_wiki', 'license_name'
        ])
        for username in usernames:
            repos = get_user_repos(username)
            for repo in repos:
                if isinstance(repo, dict): 
                    license_name = repo.get('license', {}).get('key', '') if repo.get('license') else ''                    
                    writer.writerow([
                        username,
                        repo.get('full_name', ''),
                        repo.get('created_at', ''),
                        repo.get('stargazers_count', ''),
                        repo.get('watchers_count', ''),
                        repo.get('language', ''),
                        str(repo.get('has_projects', False)).lower(),
                        str(repo.get('has_wiki', False)).lower(),
                        license_name
                    ])
                    print(f"Wrote Repo to CSV: {repo.get('full_name', '')} for {username}")
                else:
                    print(f"Skipping invalid repo data for user {username}")


if __name__ == "__main__":
    usernames = []
    with open(r"xxxx", mode='r', encoding='utf-8') as file: # Path to your users.csv
        reader = csv.DictReader(file)
        usernames = [row['login'] for row in reader]
    write_repositories_csv(usernames)
    print("CSV file 'repositories.csv' has been created successfully.")
