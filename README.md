GitHub Repository Analyzer 🔍

A Python-based tool that uses the GitHub REST API to analyze a user's public GitHub profile and repositories.

The project retrieves GitHub data, processes it using Python, and generates useful insights such as repository statistics, programming language usage, and top repositories based on stars.

🚀 Features
Fetch GitHub user profile information
Retrieve all public repositories
Handle API pagination
Analyze programming language usage
Calculate repository statistics
Calculate total stars and forks
Calculate average stars per repository
Find the most-starred repository
Display the top 5 repositories
Export the analysis results to a JSON file
Handle API and connection errors
🛠️ Technologies Used
Python
Requests
GitHub REST API
JSON
Git & GitHub
📊 Information Analyzed

The analyzer provides:

GitHub Profile
Username
Name
Followers
Following
Public repositories
Repository Statistics
Total repositories
Total stars
Total forks
Average stars
Most-starred repository
Language Analysis

The project counts the programming languages used across the user's repositories and displays their percentage distribution.

Top Repositories

Displays the top 5 repositories based on the number of stars.

📁 Project Structure
github-repository-analyzer/
│
├── github_analyzer.py
├── github_report.json
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/Aviralmallick/GitHub-Repository-Analyzer

Move into the project directory:

cd github-repository-analyzer

Install the required library:

pip install requests
▶️ How to Run

Run the Python program:

python github_analyzer.py

Enter a GitHub username when prompted:

Enter the Username: octocat

The program will retrieve and analyze the user's public GitHub data.

📄 Output

The project displays the analysis in the terminal and exports the results to:

github_report.json

The JSON report contains:

Profile information
Repository statistics
Language usage
Top repositories
Repository details such as stars, forks, language, and URL
🧠 What I Learned

Through this project, I practiced:

Working with REST APIs
Sending HTTP requests using Python
Parsing JSON responses
Writing reusable functions
Handling API errors and exceptions
Working with lists and dictionaries
Implementing pagination
Sorting and analyzing data
Exporting structured data to JSON
🔮 Future Improvements

Possible future improvements include:

Add a graphical dashboard
Add data visualization using Pandas and Matplotlib
Compare multiple GitHub users
Analyze repository activity over time
Add more detailed repository metrics
👨‍💻 Author

Aviral Mallick

B.Tech – Computer Science & Technology
