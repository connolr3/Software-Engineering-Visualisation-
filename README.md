# Software-Engineering-Visualisation-
Software Engineering Metric Visualisation Project for CSU33012 Software Engineering at TCD
Brief;
Interrogate the GitHub API to build visualisation of data available tht elucidates some aspect of the softare engineering process, such as a social graph of developers and projects, or a visualisation of indiviudal of team performance. Provide a visualisation of this using the d3js library. See https://d3js.org


It might be necessary to run 

                    pip install python-nvd3
                    
in the command line to install the Chart Library for d3.js if not already installed

The visualisation takes only the latest 30 commits and latest 30 repos for an organisation. 
I thought this was enough information for the visualisation to be effective
However, to display the latest 50 repos, for example, the repo URL can be changed from

    repos_url = 'https://api.github.com/orgs/' + org_name + '/repos'

to

    repos_url = 'https://api.github.com/orgs/' + org_name + '/repos?per_page=50'

