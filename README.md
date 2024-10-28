# IITM - Tools In Data Science - Project 1


## For my peers -

1. An explanation of how I scraped the data
- This script retrieves GitHub user data for those located in Moscow with over 50 followers, along with details of each user's repositories.
2. The most interesting and surprising fact I found after analyzing the data
- The most surprising finding from the data was that a significant number of high-follower users were from smaller startups or solo projects, not large companies.
3. An actionable recommendation for developers based on my analysis
- Developers seeking visibility should optimize their profiles by consistently updating projects and using keywords, as these factors likely attract followers.

---

# Project Overview

This project scrapes data from the GitHub API to gather information on users in Moscow with a follower count above a set threshold and their associated repositories. The extracted data is written to CSV files for easy analysis. The project is divided into two parts:

1. *User Scraper*: Collects user data (e.g., name, company, bio, number of followers, and public repositories).
2. *Repository Scraper*: Retrieves details about each user's repositories (e.g., repository name, creation date, language, and license information).

## How to Use

1. Place your GitHub access token in the `TOKEN` variable in both scripts.
2. Run the first script to retrieve and store user data in `users.csv`.
3. Run the second script, which reads usernames from `users.csv` and writes repository information to `repositories.csv`.

