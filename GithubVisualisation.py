# -*- coding: utf-8 -*-

import configparser
import requests
import json
#from nvd3 import pieChart
from nvd3 import discreteBarChart
import os
import webbrowser
from operator import itemgetter


#read config
config = configparser.ConfigParser()
config.read('GithubCredentials.ini')
token = config['Github']['token']
org_name = config['Github']['org_name']
username = config['Github']['username']

print ("token:" + token)
print ("organisation name:" + org_name)
print ("username:" + username)

 
# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to an org
#repos_url = 'https://api.github.com/user/repos'
print ("Calling APIs for Repo Names and commits")
repos_url = 'https://api.github.com/orgs/' + org_name + '/repos'
#change defualt 30 repos using 'per_page' value
#repos_url = 'https://api.github.com/orgs/' + org_name + '/repos?per_page=50'
repos = json.loads(gh_session.get(repos_url).text)


repo_count = 0

#initalise arrays
all_data = []
x_data = []
y_data = []

for repo in repos:
    curr_data = []
    print ("repo name: " + repo['name'])
    commits_url = 'https://api.github.com/repos/' + org_name + '/' + (repo['name']) +'/commits'
    curr_data.append(repo['name'])
    
    commits = json.loads(gh_session.get(commits_url).text)
    commit_count = 0
    
    for commit in commits:
        #print (commit['commit']['author']['name'])
        commit_count+=1
    
    print ("total commits: " + str(commit_count))
    curr_data.append(commit_count)

    print ("")
    repo_count+=1
    all_data.append(curr_data)
    
    
print ("finished API processing")   


print("running report")
report_name = 'github-report.html'

#sort array
#print(all_data)
all_data = sorted(all_data, key=itemgetter(1))
#print(all_data)

print("iterate")
alldata_count = 0
while alldata_count < int(len(all_data)):
    x_data.append(all_data[alldata_count][0])
    y_data.append(all_data[alldata_count][1])
#    print(all_data[alldata_count][0])
 #   print(all_data[alldata_count][1])
    alldata_count += 1

#Open File to write the D3 Graph
output_file = open(report_name, 'w')

chart_type = 'discreteBarChart'
chart = discreteBarChart(name=chart_type, height=500, width=5000)
title = 'Github BarChart showing Repo commits for ' + org_name + ' with ' + str(repo_count) + ' repos'
chart.set_containerheader("\n\n<h2>" + title + "</h2>\n\n")
chart.add_serie(y=y_data, x=x_data)
chart.buildhtml()
chart_html = chart.htmlcontent

output_file.write(chart.htmlcontent)

#close Html file
output_file.close()
print("finished report");

path = os.path.abspath(report_name)

url = 'file://' + path


webbrowser.open(url)
#