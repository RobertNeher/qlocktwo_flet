import json
import io
import flet as ft
import time
import argparse
from tools import roundedTime
from watch_face import watchFace


def main(page: ft.Page):
    settings = json.load(
        io.open("./assets/settings.json", "r", encoding="UTF-8"))["settings"][0]
    page.title = "QlockTwo"
    page.padding = 50
    page.window.width = 700
    page.window.height = 675
    page.bgcolor = ft.colors.WHITE24
    page.update()

    # parser = argparse.ArgumentParser(prog="QlockTwo", usage="%(prog)s [options]")
    # parser.add_argument("-m", "--minute", nargs="?", help="Minute", type=int)
    # parser.add_argument("-o", "--hour", nargs="?", help="Hour", type=int)
    # args = parser.parse_args()

    while True:
        timeStr = roundedTime(denominator=5, roundUp=False)

        if len(page.controls) >= 1:
            del page.controls[-1]

        page.add(
            # watchFace(hour=args.hour, minute=args.minute, settings=settings)
            watchFace(hour=int(timeStr[0:2]), minute=int(timeStr[3:5]), settings=settings)
        )
        page.expand = 1
        page.update()
        time.sleep(5)

ft.app(main, assets_dir="./assets")
