# RCCLI Overview

RCCLI is a command line interface for interacting with the Recurse Center API. Currently, it only 
contains a small subset of the API's functionality as a demonstration. Because it provides access to
internal Recurse Center information, it will only work for Recurse Center members who can set up 
proper authorization.

## Setup Instructions
### Authorization (for Recurse Center members only)
1. Create a personal access token at https://www.recurse.com/settings/apps
1. Check out this project from GitHub.
1. Replace the sample token stored in `PERSONAL_ACCESS_TOKEN` in the project file 
   `src/authentication/config.py` with your personal token. 
   - Please make sure you DO NOT upload your token to github at any time!


### Installation
It's recommended (but not required) that you install this into a virtual environment. Do this step
after you've set up the authorization above.

1. In your terminal, CD into the project directory.
1. If using a virtual environment, create and activate the virtual environment.
1. Run `pip install .` to install what is in your current directory as a python package.
    - This will also install the package dependencies, `click` and `requests`. 

## Usage
As long as you are in your virtual environment, you should be able to use this tool by calling 
`rccli`.

For any command or sub-command, use the `--help` flag to see documentation about what the tool can 
do.

### Examples
Using the help flag on the top-level command:
```bash
$ rccli --help
Usage: rccli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  profile  Interact with RC profiles
```

Using the help flag on a sub-command:
```bash
$ rccli profile search --help
Usage: rccli profile search [OPTIONS]

  Returns all names/pronouns/email addresses from profiles fitting a given
  search criteria

Options:
  --query-string TEXT             Search by name, skills, or profile questions
  --batch-id INTEGER              Search by batch ID
  --role [recurser|resident|facilitator|faculty]
                                  Filter by RC role
  --scope [current|overlap]       Filter by status
  --help                          Show this message and exit.
```

Note also that multiple options can be used at once when using a command:
```bash
$ rccli profile search --role faculty --scope current
Example Name (They/them) - example@example.com
Another Name (She/her) - another@example.com
OneLast Name (He/him) - onelast@example.com
```

## Contributing
This project was created as for demonstration purposes. If you'd like to add functionality, please 
feel free to clone the project and edit as you see fit! I'd love to see what you come up with!
