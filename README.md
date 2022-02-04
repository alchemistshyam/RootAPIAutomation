# Root API AUTOMATION

## Environment 
1. Python 3+
2. Generate token from https://gorest.co.in/
2. pre-commit

## Steps to fetch token
1. Open https://gorest.co.in/
2. Sign up
3. Generate a token
4. Clone the project
5. Change the text "xyz" to the token from Step 3 in config/cred.json
6. Save the cred.json file.

## Installation
1. pip3 install -r requirements.txt

## Commands
pytest -s -v --junitxml=api_report.xml --html=api_report.html --log-cli-level info --log-file=api_report.log

## Jira Ticket Command
python lib/jira_helper.py --username=shyamsingh.mit@gmail.com --token=xyztoken --server=https://roottechnology.atlassian.net --operation=create --error_file=api_report.log --label=API_Automation