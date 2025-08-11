# CFCli Official Documentation Page

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Setup](#setup)
- [Command Format](#command-format)
- [Commands](#commands)

## Installation

Head to [the pypi page](https://pypi.org/project/cfcli-py-tool/) and copy the command at the top.

In our case it will be `pip install cfcli-py-tool`.

Open your terminal (or command line if you're using windows) and paste the following:

```bash
pip install cfcli-py-tool
```

If this gives an error, please try:

```bash
pip3 install cfcli-py-tool
```

This will install CFCli from the PyPi package manager.

In order to test your installation, please run:

```bash
cf-cli
```

## Requirements

Since the project is a pip (python package manager) package, you are required to have the following in order for it to work.
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

## Commands

CFCli has a few very simple commands.

### Base

The base command with so subcommands no flags is just `cf-cli`. This is the welcome/startup text.

### Help

By running,

```bash
cf-cli help
```

You will be able to see each of the subcommands provided by CFCli that you can use. They include, help, user, contests, problemset, rating, and streak

### User

The `user` subcommand lets you view the stats of a user registered on Codeforces. It shows their hande, max rating, current rating (with its appropriate colour), the title image (ie profile picture), country, name, as well as contribution

Usage:

```bash
cf-cli user <username>
```

Here is the output for the Codeforces user [tourist](https://codeforces.com/profile/tourist) by running the command `cf-cli user tourist` (the output is subject to change as ratings and metadata changes).

```bash
 Username      tourist              ╭─────── Title Photo ────────╮
 Country       Belarus              │                            │
 Name          Gennady Korotkevich  │      View Title Photo      │
 Max Rating    4009                 │                            │
 Contribution  106                  ╰────────────────────────────╯
```

### Contests

The contests command lets you view the upcoming contest on Codeforces that are available to view on [the website](https://codeforces.com/contests). The command formats them in a table and has the contest id, the name of the contest, and the time until start (in seconds).

Here is an example output that is shown by running `cf-cli contests`:

```bash
            Upcoming Codeforces Contests
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ ID   ┃ Name                      ┃ Start in (sec) ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ 2132 │ Codeforces Round (Div. 3) │ 917534         │
└──────┴───────────────────────────┴────────────────┘
```

### Problemset

If you want to see the last *x* problems in the codeforces problemset, you can do so by running:

```bash
cf-cli problemset -count <number>
```

This shows the last <number> problems on the problemset.

Here is an example output

```bash
                               First 2 Codeforces Problems
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ID    ┃ Name               ┃ Points ┃ Tags                                             ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 2131H │ Sea, You & copriMe │    N/A │ brute force, graphs, greedy, math, number theory │
│ 2131G │ Wafu!              │    N/A │ bitmasks, brute force, dp, math                  │
└───────┴────────────────────┴────────┴──────────────────────────────────────────────────┘
```
This was the output I recieved when I ran `cf-cli problemset -count 2`. **These outputs are subject to change since the problemset changes actively**

### Rating

The rating command is used to show the rating history of a particular user on the platform. More specifically, it shows their ratings in each contest they've attended so far.

The command to use the rating subcommand is `cf-cli rating <user>`

Here is the sample for user *poetaio*

```bash
                         poetaio's Rating History
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┓
┃ Contest Name                   ┃ Rank ┃ Old Rating ┃ New Rating ┃ Delta ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━┩
│ Codeforces Round 919 (Div. 2)  │ 8453 │          0 │        447 │  +447 │
│ Codeforces Round 1032 (Div. 3) │ 9605 │        447 │        740 │  +293 │
└────────────────────────────────┴──────┴────────────┴────────────┴───────┘
```

Not only that, but it also shows their rating graph through matplotlib.