from datetime import datetime
from jira import JIRA
import logging
import sys

import argparse# Create the parser

parser = argparse.ArgumentParser()
logger = logging.getLogger()


parser.add_argument('--username', type=str, required=True)
parser.add_argument('--token', type=str, required=True)
parser.add_argument('--server', type=str, required=True)
parser.add_argument('--operation', type=str, required=True)
parser.add_argument('--error_file', type=str, required=True)
parser.add_argument('--label', type=str, required=False)

args = parser.parse_args()

print("Setting up Environment")

user_name = args.username
api_token = args.token
server = args.server
print(f"Username : {user_name} , api_token : {api_token} , server : {server}  ")

jira = JIRA(basic_auth=(user_name, api_token), 
                    options={"server": server})
    
print(f"Operation : {args.operation}")
if args.operation == "create" :
    print(f"Error File : {args.error_file}")
    
    file_name = args.error_file
    error_data = ""
    with open(file_name) as f:
            error_data = f.read()
    summary = args.label + " - " + str(datetime.now())
    test_data = {
        "project": "ROOTTECH",
        "summary": summary,
        "description": error_data,
        "issuetype": {"name": "Bug"},
        "labels" : [args.label]
    }

    issue_key = jira.create_issue(fields=test_data)
    print(f"Ticket Link   :   {server}/browse/{issue_key}")