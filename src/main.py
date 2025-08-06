import sys
from rich.console import Console
from rich.panel import Panel

from commands.help import run as help
from commands.user import run as user
from commands.contests import run as contests
from commands.problemset import run as problemset
from commands.rating import run as ratings

import typing

console = Console()

def intro() -> None:
    """
    The startup message/dialogue for the program
    """
    console.print(Panel.fit(
        "[bold cyan]cf-cli[/bold cyan]\n\n"
        "A CLI tool for interacting with the Codeforces API.\n\n"
        "Run [yellow]cf-cli help[/yellow] for available commands.",
        title="Welcome to cf-cli!"
    ))
    
def main() -> None:
    """
    The main function ie the entry point for the cf cli system
    """
    if len(sys.argv) == 1:
        intro()
        return

    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command == "help":
        help(args)
    elif command == "user":
        user(args)
    elif command == "contests":
        contests(args)
    elif command == "problemset":
        problemset(args)
    elif command == "rating":
        ratings(args)
    else:
        console.print(f"[red]Unknown command:[/red] {command}")
        console.print("Run [yellow]cf-cli help[/yellow] for help.")

if __name__ == "__main__":
    main()