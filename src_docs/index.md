# CFCli Official Documentation Page

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Setup](#setup)
- [Command Format](#command-format)

## Installation

**Keep in mind that Windows is the only supported OS for now (due to cross-system issues)**

- Go to the [latest install](https://github.com/CompProgTools/CFCli/releases) of CF-Cli on the repository
- Download the latest install for your specifc operating system
- Copy the pathname of your install location (.exe, .app, etc)

Now you will make the commands accessible by a global command.

If you're on windows, try the following:

- Copy the pathname of your installation
- Press Windows + S
- Type in `Edit the system environment variables`
- Once in there, click on `Environment Variables`
- Under `System Variables`, select Path and click Edit
- Click **New** and paste the path that you copied
- Save everything and exit

Once that's done, restart your terminal and you're good to go.

Now you can test your installation by running:

```bash
cf-cli
```

## Requirements

The requirements for CF-Cli are pretty simple since most of the work is done by script itself and uses the Codeforces API to get raw data (These requirements are if you're either doing development, or building from source):
- Python 3.8+
- Latest Pip version

## Setup

The setup for cf-cli is very minimal. Since there are parts of the [Codeforces API](https://codeforces.com/apiHelp) that require authentication, it is the only environment variable that is needed.

## Command Format

The format for CF-Cli is quite simple. The base command is `cf-cli` and by running it, you will get the start command as a greeting. After that, you are required to use subcommands as every other command is considered a subcommand in the program.

Here is the format for subcommand requests

```bash
cf-cli `subcommand` {data} `--flag`
```

Keep in mind that flags are optional and not needed.