# PyBlankProject
Blank Project For Python

You need to have the pre-commit package manager installed.

Using pip:

pip install pre-commit
In a python project, add the following to your requirements.txt (or requirements-dev.txt):

pre-commit
As a 0-dependency zipapp:

locate and download the .pyz file from the github releases
run python pre-commit-#.#.#.pyz ... in place of pre-commit ...
Quick start
1. Install pre-commit
follow the install instructions above
pre-commit --version should show you what version you're using
$ pre-commit --version
pre-commit 4.3.0
2. Add a pre-commit configuration
create a file named .pre-commit-config.yaml
you can generate a very basic configuration using pre-commit sample-config
the full set of options for the configuration are listed below
this example uses a formatter for python code, however pre-commit works for any programming language
other supported hooks are available
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
    -   id: black
3. Install the git hook scripts
run pre-commit install to set up the git hook scripts
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
now pre-commit will run automatically on git commit!
