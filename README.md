# Github-Project-Initialization-Automation

## Process:
- Install Python
- Download PyGithub Package for Python
- Generate Github Token(which has repo read/write access) or use login_id and password to login.
  (This project uses the token method)
- Search `Edit the system environment variables` in windows menu and set environment variable for **Github Token** as `GithubToken` and **directory** where you create projects as     `MainProjectPath`. (use frontslash while writing directory path instead of backslash)
- Download both the files from this repository and paste it in `C:\Windows\System32`.
- Now, you can create repository on **Github**(with readme and initial commit) as well as **local folder**(of the same name with git initialized in the directory stated in the       MainProjectPath).
- Command for creating only **local folder**:
  `create <foldername>`
- Command for creating **Github Repo** as well as **local folder**:
  `create <foldername> g`
- For help with this command in cmd, use:
  `create --help`
