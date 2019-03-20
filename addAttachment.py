from urllib2 import HTTPError
import requests



username = 'YOUSERNAME'
password = 'PASSWORD'

# New Issue Variables:
issueProjectKey = "PROJECTKEY"
issueNr = "ISSUE_NUMBER"
issueKey = issueProjectKey+"-"+issueNr
projectURL = 'JIRASERVER/jira'
attachmentURL = projectURL + "/rest/api/2/issue/" + issueKey + "/attachments"

file = "FILEPATH\Test.PNG"

pngfile = {'file': open(file, 'rb')}

headers2 = {'X-Atlassian-Token': 'no-check'}
print "Upload image ..." 
s = request.Session() 
try:
    js_res = s.post(attachmentURL, auth=(username, password), files=pngfile, headers=headers2, verify=False)
    print js_res.status_code
except HTTPError, error:
    print error
