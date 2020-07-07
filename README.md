# Github-Project-Initialization-Automation

## Process:

- Install Python
- Download PyGithub Package for Python \
  `pip install PyGithub`
- Generate Github Token(which has repo read/write access) or use login_id and password to login.
  (This project uses the token method)
- Search `Edit the system environment variables` in windows menu and set environment variable for **Github Token** as `GithubToken` and **directory** where you create projects as `MainProjectPath`. (Use frontslash while writing directory path instead of backslash)
- Now, `git clone "https://github.com/ashutoshanand139/Github-Project-Initialization-Automation.git"`
- Add this folder directory to `PATH`

---

- Now, you can create repository on **Github** (with readme and initial commit) as well as **local folder** (of the same name with git initialized in the directory stated in the MainProjectPath).
- Command for creating only **local folder**: \
  `create <foldername> -l`
- Command for creating **public Github Repo** as well as **local folder**: \
  `create <foldername>`
- Command for creating **private Github Repo** as well as **local folder**: \
  `create <foldername> pr`
- For help or for more commands, use: \
  `create --help`
