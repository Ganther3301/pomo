#!/usr/bin/python3
from time import sleep
import sys

from plyer import notification

import typer

from rich.emoji import Emoji
from rich.table import Column
from rich.progress import (
    BarColumn,
    Progress,
    TaskProgressColumn,
    TextColumn,
    TimeRemainingColumn,
)

app = typer.Typer()

def get_layout(mode: str):
    layouts = {
        'work':(
            TextColumn("[red]Work Time![/red]", justify="right"),
            'Time to start working!',
            25*60 
        ),

        'break':(
            TextColumn("[green]Break Time![/green]", justify="right"),
            'Time for a break!',
            5*60
        ),
    }

    return layouts[mode]

def main():
    """
    A simple, CLI pomodoro timer. 
    """
    try:
        # mins = 1497
        pomos = [Emoji('tomato'), Emoji('tomato'),Emoji('tomato'),Emoji('tomato')]
        
        while pomos:
            for i in range(8):
                modes = {0: 'work', 1: 'break'}
                text_column, notification_title, mins = get_layout(modes[i%2])

                progress = Progress(
                    text_column,
                    BarColumn(),
                    TaskProgressColumn(),
                    "•",
                    TimeRemainingColumn(),
                    "•",
                    TextColumn(' '.join(map(lambda x: str(x), pomos))),
                    transient= True
                )

                notification.notify(title=notification_title, message= ' '.join(map(lambda x: str(x), pomos)) , app_name='pomo')
                with progress:
                    for n in progress.track(range(mins)):
                        sleep(1)

                if i%2:
                    pomos.pop()

        print("Good Job!")

    except :
        print("Goodbye!")
        sys.exit()

if __name__ == '__main__':
    typer.run(main)
