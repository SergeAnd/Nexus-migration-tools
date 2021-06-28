'''
############################################################################
You should add this string

    nexus.scripts.allowCreation=true

to nexus.properties file before you start this script

Also, you must store your credentials strong.
!!! Do not commit this file to public repositories with your credentials.
############################################################################
'''

import nexuscli
import os
from datetime import datetime

nexus_config = nexuscli.nexus_config.NexusConfig({
    "api_version": "v1",
    "password": "admin123",
    "url": "http://10.0.0.30:8081/",
    "username": "admin",
    "x509_verify": True
})
nexus_config.load()
nexus_client = nexuscli.nexus_client.NexusClient(config=nexus_config)

rootpath = "G:\\tmp\\"

for repo in nexus_client.repositories.list:
    if repo['type'] == 'hosted':
        print(repo)

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input('Download all repositories? [Y/n]').lower()
if choice in yes:
    for repo in nexus_client.repositories.list:
        if repo['type'] == 'hosted':
            file_path = rootpath + repo['name'] + "\\"
            directory = os.path.dirname(file_path)
            try:
                os.stat(directory)
            except:
                os.mkdir(directory)
            print("\n", repo['format'], repo['url'], directory)
            print('Starting download repository', repo['name'], 'at', str(datetime.now()))
            nexus_client.repositories.get_by_name(repo['name']).download('/', file_path)
            print('Download repository', repo['name'], 'finished at', datetime.now(), "\n")
elif choice in no:
    onerepo = input('Write reponame without quotes:').lower()
    for repo in nexus_client.repositories.list:
        if repo['type'] == 'hosted':
            if str(repo['name']) == str(onerepo):
                file_path = rootpath + repo['name'] + "\\"
                directory = os.path.dirname(file_path)
                try:
                    os.stat(directory)
                except:
                    os.mkdir(directory)
                print("\n", repo['format'], repo['url'], directory)
                print('Starting download repository', repo['name'], 'at', str(datetime.now()))
                nexus_client.repositories.get_by_name(repo['name']).download('/', file_path)
                print('Download repository', repo['name'], 'finished at', datetime.now(), "\n")
            else:
                continue
else:
    print("Please respond with 'yes' or 'no' only")
    print("I DUNNO What you mean. Stopping script...")