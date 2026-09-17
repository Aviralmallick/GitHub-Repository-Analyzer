import requests
import json

def get_user_data(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    response.raise_for_status()
    data = response.json()
    return data

def get_repositories(username):
    all_repos = []
    page = 1

    while True:
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            params={
                "per_page": 100,
                "page": page
            }
        )

        response.raise_for_status()

        repos = response.json()

        if not repos:
            break

        all_repos.extend(repos)

        page += 1

    return all_repos

def analyze_languages(repos):
    lang_count = {}
    for repo in repos:
        language = repo['language']
    
        if language is None:
            continue
    
        if language not in lang_count:
                lang_count.update({language:1})
        else:
            lang_count.update({language:lang_count[language]+1})    
    
    lang_count_sorted = dict(sorted(lang_count.items(),key = lambda item:item[1],reverse=True)) 
    return lang_count_sorted   

def get_top_repositories(repos):
    sorted_repos = sorted(
        repos,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    return sorted_repos[:5]


def analyze_repositories(repos):
    # ========== Repository Statistics ==========
    total_repos = 0
    total_stars = 0
    total_forks = 0
    most_starred_count = 0
    most_starred_repo = ''
    for repo in repos:
        total_repos += 1
        total_stars = total_stars + repo['stargazers_count']
        total_forks = total_forks + repo['forks_count']

        if repo['stargazers_count'] > most_starred_count:
            most_starred_count = repo['stargazers_count']
            most_starred_repo = repo['name']

    if total_repos > 0:
        average_stars = total_stars/total_repos
    else:
        average_stars = 0    

    return {
    "total_repos": total_repos,
    "total_stars": total_stars,
    "total_forks": total_forks,
    "average_stars": average_stars,
    "most_starred": most_starred_repo,
    "most_starred_count": most_starred_count
}

def export_results(user_data, repo_stats, language_stats, top_repos):

    report = {
        "profile": {
            "username": user_data["login"],
            "name": user_data["name"],
            "followers": user_data["followers"],
            "following": user_data["following"],
            "public_repositories": user_data["public_repos"]
        },

        "repository_statistics": repo_stats,

        "language_usage": language_stats,

        "top_repositories": [
            {
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo["language"],
                "url": repo["html_url"]
            }
            for repo in top_repos
        ]
    }

    with open("github_report.json", "w") as file:
        json.dump(report, file, indent=4)

def main():
    username  = input("Enter the Username: ")
    try:
        user_data = get_user_data(username)
        repos = get_repositories(username)
    except requests.exceptions.HTTPError:
        print("GitHub user not found or API request failed.")
        return 
    except requests.exceptions.RequestException:
        print("Something went wrong while connecting to GitHub.")
        return   
    lang_count_sorted = analyze_languages(repos)
    stat = analyze_repositories(repos)
    top_repos = get_top_repositories(repos)
    export_results(user_data,stat,lang_count_sorted,top_repos)
    
    print("========== GitHub Profile ==========")
    print("Username:", user_data["login"])
    print("Name:", user_data["name"])
    print("Followers:", user_data["followers"])
    print("Following:", user_data["following"])
    print("Public Repositories:", user_data["public_repos"])


    print("========== Language Usage ==========")
    total_no_of_languages = sum(lang_count_sorted.values())
    for lang,value in lang_count_sorted.items():
        percentage = round(value/total_no_of_languages*100,1)
        print(f"{lang} : {percentage} %")

    print("========== Repository Statistics ==========")    
    total_repo = stat['total_repos']
    total_stars = stat['total_stars']
    total_forks = stat['total_forks']
    average_stars = stat['average_stars']
    most_starred = stat['most_starred']
    most_starred_count = stat['most_starred_count']
    print("Total Repositories: ",total_repo)
    print("Total Stars: ",total_stars)
    print("Total Forks: ",total_forks)
    print("Average Stars",average_stars)
    print("Most Starred Repository: ",most_starred)
    print("Most Starred Repository Count: ", most_starred_count)

    print("========== Top 5 Repositories ==========")
    for i, repo in enumerate(top_repos, start=1):
        print(f"{i}. {repo['name']} : ⭐ {repo['stargazers_count']}")


if __name__ == "__main__":
    main()