from github import Github as ghb
import sys
import os

foldername = str(sys.argv[1])

try:
  flag = str(sys.argv[2])
except:
  flag = ""

try:
  status = str(sys.argv[3])
except:
  status = ""  

path = os.environ.get('MainProjectPath')          
new_dir = path + foldername

if foldername == "":
  print(">> Please use proper format.")
  print(">> Run \"create --help\" for instructions.")

elif flag == "" or flag == "-gl" or flag == "-lg" or flag == "-pb":
  try:
    os.mkdir(new_dir)
    os.chdir(new_dir)
    token = os.environ.get('GithubToken')
    user = ghb(token).get_user()
    login = user.login

    if status == "" or status == "-pb":
      repo = user.create_repo(foldername)
      commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']
      for c in commands:
        os.system(c)
      print(f'{foldername} created locally as well as an public repository on Github.')
      os.system('code .')

    elif status == "-pr":
      repo = user.create_repo(foldername, private=True)
      commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']
      for c in commands:
        os.system(c)
      print(f'{foldername} created locally as well as an private repository on Github.')
      os.system('code .')

    else:
      print(">> Please use proper format.")
      print(">> Run \"create --help\" for instructions.")  

  except:
    print("This foldername already exists.")

elif flag == "-pr":
  try:
    os.mkdir(new_dir)
    os.chdir(new_dir)
    token = os.environ.get('GithubToken')
    user = ghb(token).get_user()
    login = user.login
    repo = user.create_repo(foldername, private=True)
    commands = [f'echo # {repo.name} >> README.md',
          'git init',
          f'git remote add origin https://github.com/{login}/{foldername}.git',
          'git add .',
          'git commit -m "Initial commit"',
          'git push -u origin master']
    for c in commands:
      os.system(c)
    print(f'{foldername} created locally as well as an public repository on Github.')
    os.system('code .')  
  except:
    print("This foldername already exists.")    

elif flag == "-l":
  if status == "":
    try:
      os.mkdir(new_dir)
      os.chdir(new_dir)
      os.system(f'echo # {foldername} >> README.md')
      print(f'{foldername} created locally.')
      os.system('code .')
    except:
      print("This foldername already exists.")    
  else:
    print(">> Please use proper format.")
    print(">> Run \"create --help\" for instructions.")


elif flag == "-g":
  if status == "" or status == "-pb":
    token = os.environ.get('GithubToken')
    user = ghb(token).get_user()
    login = user.login
    repo = user.create_repo(foldername)
    print(f'{foldername} public repository created on Github.')
  elif status == "-pr":
    token = os.environ.get('GithubToken')
    user = ghb(token).get_user()
    login = user.login
    repo = user.create_repo(foldername, private=True)
    print(f'{foldername} private repository created on Github.')
  else:
    print(">> Please use proper format.")
    print(">> Run \"create --help\" for instructions.")

else:
  print(">> Please use proper format.")
  print(">> Run \"create --help\" for instructions.")
  
    
