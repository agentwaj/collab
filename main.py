import os
import subprocess
import sys

email = sys.argv[1]
name = email.split("@", 1)[0]

env = os.environ.copy()
env["GIT_AUTHOR_NAME"] = name
env["GIT_AUTHOR_EMAIL"] = email
env["GIT_COMMITTER_NAME"] = name
env["GIT_COMMITTER_EMAIL"] = email

with open("collaborators.txt", "a") as f:
    f.write(email + "\n")

subprocess.run(["git", "commit", "-am", "Update"], check=True, env=env)
subprocess.run(["git", "push"], check=True)