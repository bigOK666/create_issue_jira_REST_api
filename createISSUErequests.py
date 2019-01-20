from json import dumps
import requests
from requests.auth import HTTPBasicAuth

username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'

issueProjectKey = "PROJECTKEY"
issueSummary = "Create Issue with requests"
issueDescription = "Login and Issue creation test requests"
issueTypeName = "Test"

projectURL = 'JIRA_SERVER/jira'
createIssueURL = projectURL + "/rest/api/2/issue/"

headers = {"Content-Type": "application/json"}
print "Creating Issue ..."

values = dumps({
    "fields": {
        "project": {
            "key": issueProjectKey
        },
        "summary": issueSummary,
        "description": issueDescription,
        "issuetype": {
            "name": issueTypeName
        },
        "labels": [
            "testCreateLabel"
        ],
        "priority": {
            "name": "Minor"
        },
        "assignee": {
            "name": username
        }
    }
})


try:
    r = requests.post(createIssueURL, data=values, headers=headers, auth=HTTPBasicAuth(username,password), verify=False)
    print r.status_code
    contentObject = r.json()
    print contentObject['key']
except requests.exceptions.HTTPError as error:
    print error


