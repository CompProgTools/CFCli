import sys
from rich.console import Console
from rich.panel import Panel

from commands.help import run as help
from commands.user import run as user
from commands.contests import run as contests


console = Console()

def intro():
    console.print(Panel.fit(
        "[bold cyan]cfcli[/bold cyan]\n\n"
        "A CLI tool for interacting with the Codeforces API.\n\n"
        "Run [yellow]cfcli help[/yellow] for available commands.",
        title="Welcome to cfcli!"
    ))
    
def main():
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
    else:
        console.print(f"[red]Unknown command:[/red] {command}")
        console.print("Run [yellow]cfcli help[/yellow] for help.")

if __name__ == "__main__":
    main()