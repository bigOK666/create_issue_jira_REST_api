#read links(clones/is cloned by) from issues and write the results in excel

#log in using API
from jira import JIRA
options = {'server':'https....'}
jira = JIRA(options, basic_auth=(config.USER, config.PASS)
#read the ticket from Excel which contains KEY-WORD

#check the KEY of the ticket in Jira and store the link(issue-key and summary) of "clones" in a cell of the same row

#end the session

#search the issue-key from link in Excel and write the issue-key and summary which contains KEY-WORD in the same row
