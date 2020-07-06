from github import Github as ghb
import sys
import os

foldername = str(sys.argv[1])

try:
  flag = str(sys.argv[2])
except:
  flag = ""

path = os.environ.get('MainProjectPath')          
new_dir = path + foldername

if foldername == "":
  print("Use proper format")

elif flag == "":
  try:
    os.mkdir(new_dir)
    os.chdir(new_dir)
    os.system(f'echo # {foldername} >> README.md')
    print(f'{foldername} created locally.')
    os.system('code .')
  except:
    print("This foldername already exists.")    

elif flag == "g":
  try:
    os.mkdir(new_dir)
    os.chdir(new_dir)
    token = os.environ.get('GithubToken')
    user = ghb(token).get_user()
    login = user.login
    repo = user.create_repo(foldername)

    commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']

    for c in commands:
      os.system(c)

    print(f'{foldername} created locally as well as an repository on Github.')
    os.system('code .')
  
  except:
    print("This foldername already exists.")
    
