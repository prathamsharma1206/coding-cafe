# Lab 4 — Git & GitHub

## Question 1
`--global` means that the Git username and email settings apply across all repositories for my user account. If I leave it out, the settings apply only to the current repository.

## Question 2
The `.git` directory appeared in `ls -a` but not in `ls`. It contains Git's internal information for the repository, including its history, configuration, references, and staging information.

## Question 3
Git offered approximately [FILL THIS IN FROM YOUR EARLIER git status OUTPUT] files and folders to track. [Mention whether anything appeared that you did not write, such as files inside `.venv/`.]

## Question 4
After creating `.gitignore`, the files inside `.venv/` and other ignored Python/cache or system files disappeared from the untracked list. Git now knows to ignore those files and folders.

## Question 5
Yes, `.gitignore` should be committed. It is a project configuration file that tells Git which files should be ignored, so other people working with the repository need to have it too.

## Question 6
`README.md` moved from “Untracked files” to “Changes to be committed.” In the three-places model, `git add README.md` moved it from the working directory to the staging area.

## Question 7
Git reported that the commit was created successfully. It showed 3 files changed and 21 insertions.

## Question 8
The first seven characters of my commit hash are `44645c5`. They identify that specific commit and provide a convenient way to refer to it without typing the entire hash.

## Question 9
The four steps are: edit the files, stage the changes, commit the changes, and repeat the process.

## Question 10
`README.md` has a special name because GitHub automatically displays it on the repository's front page. It acts as an introduction to the project and explains what the repository contains.

## Question 11
`gh auth login` authenticates my GitHub account through GitHub CLI and stores authentication credentials. This allows GitHub to authenticate me without asking for my password every time I push.

## Question 12
The `README.md` file is displayed on the GitHub repository's front page. GitHub automatically renders a repository's README there so visitors can immediately see information about the project.

## Question 13
No, pushing did not change my local history. `git push` copied my existing local commits to the GitHub repository.

## Question 14
A private repository exists on GitHub but can only be accessed by the owner and people who have been given permission. If a repository does not exist on GitHub at all, there is no online repository for collaborators or TAs to acces# Lab 4 — Git & GitHub

## Question 1
`--global` means that the Git username and email settings apply across all repositories for my user account. If I leave it out, the settings apply only to the current repository.

## Question 2
The `.git` directory appeared in `ls -a` but not in `ls`. It contains Git's internal information for the repository, including its history, configuration, references, and staging information.

## Question 3
Git offered approximately [FILL THIS IN FROM YOUR EARLIER git status OUTPUT] files and folders to track. [Mention whether anything appeared that you did not write, such as files inside `.venv/`.]

## Question 4
After creating `.gitignore`, the files inside `.venv/` and other ignored Python/cache or system files disappeared from the untracked list. Git now knows to ignore those files and folders.

## Question 5
Yes, `.gitignore` should be committed. It is a project configuration file that tells Git which files should be ignored, so other people working with the repository need to have it too.

## Question 6
`README.md` moved from “Untracked files” to “Changes to be committed.” In the three-places model, `git add README.md` moved it from the working directory to the staging area.

## Question 7
Git reported that the commit was created successfully. It showed 3 files changed and 21 insertions.

## Question 8
The first seven characters of my commit hash are `44645c5`. They identify that specific commit and provide a convenient way to refer to it without typing the entire hash.

## Question 9
The four steps are: edit the files, stage the changes, commit the changes, and repeat the process.

## Question 10
`README.md` has a special name because GitHub automatically displays it on the repository's front page. It acts as an introduction to the project and explains what the repository contains.

## Question 11
`gh auth login` authenticates my GitHub account through GitHub CLI and stores authentication credentials. This allows GitHub to authenticate me without asking for my password every time I push.

## Question 12
The `README.md` file is displayed on the GitHub repository's front page. GitHub automatically renders a repository's README there so visitors can immediately see information about the project.

## Question 13
No, pushing did not change my local history. `git push` copied my existing local commits to the GitHub repository.

## Question 14
A private repository exists on GitHub but can only be accessed by the owner and people who have been given permission. If a repository does not exist on GitHub at all, there is no online repository for collaborators or TAs to access.

