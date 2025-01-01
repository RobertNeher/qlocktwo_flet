# import flet as ft
# import json
# import io
import datetime

from src.tools import roundedTime

def main():
    timeStr = roundedTime(denominator=5, roundUp=False)
    print(timeStr[0:2])
#------------------------ MAIN ------------------------#
if __name__ == "__main__":
    main()
# ft.app(main, view=ft.AppView.WEB_BROWSER)