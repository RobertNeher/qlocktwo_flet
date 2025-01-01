import json
import io
import flet as ft
import time
import signal

import argparse
# from tools import roundedTime
from src.watch_face import watchFace

# def handler(signum, frame):
#     input("Progam paused. Hit enter to resume")
#     return

def main(page: ft.Page):
    settings = json.load(
        io.open("./assets/settings.json", "r", encoding="UTF-8"))["settings"][0]
    page.title = "QlockTwo"
    page.padding = 50
    page.window.width = 700
    page.window.height = 700
    page.bgcolor = ft.colors.WHITE24
    page.update()

    # parser = argparse.ArgumentParser(prog="QlockTwo", usage="%(prog)s [options]")
    # parser.add_argument("-m", "--minute", nargs="?", help="Minute", type=int)
    # parser.add_argument("-o", "--hour", nargs="?", help="Hour", type=int)
    # args = parser.parse_args()

    textStyle = ft.TextStyle(
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.RED_300
    )

    for hour in range(12, 24):
        for minutes in range(0, 55, 5):
            if len(page.controls) >= 1:
                del page.controls[-1]

            page.add(
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            f"{hour:02d}:{minutes:02d}",
                            style=textStyle
                        ),
                        watchFace(hour=hour, minute=minutes, settings=settings)
                    ]
                )
            )
            page.expand = 1
            page.update()
            input("Next...")


ft.app(main, assets_dir="./assets")
