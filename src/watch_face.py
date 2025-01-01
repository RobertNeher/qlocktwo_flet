import flet as ft

def letter(char: str, active: bool) -> ft.Text:
    return ft.Text(
        char,
        theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
        color=ft.colors.WHITE if active else ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER,
        expand=1
    )

def watchFace(hour: int, minute: int, settings: map) -> ft.GridView:
    charGrid = ft.GridView(
        expand=1,
        runs_count=11,
        max_extent=50,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    charGrid.controls = []

    #
    # Only 12 hour clock
    #
    if hour > 12:
        hour -= 12

    minuteMask = settings["FiveMinutesMapping"][int(minute/5)][str(minute)]
    hourMask = settings["HoursMapping"][hour][str(hour)]

    for row in range(0, len(settings["qlockTwoChars"])):
        charRow = settings["qlockTwoChars"][row]
        hourRow = hourMask[row]
        minuteRow = minuteMask[row]
        for column in range(0, len(settings["qlockTwoChars"][row])):
            charGrid.controls.append(
                letter(
                    charRow[column],
                    active=charRow[column] == "1" or hourRow[column] == "1" or minuteRow[column] == "1"
                )
            )
            # AM
            if row == 5 and column == 5:
                charGrid.controls.extend(
                    [
                        letter(
                            charRow[column],
                            active=True
                        ),
                        letter(
                            charRow[column + 1],
                            active=True
                        )
                    ]
                )
                column += 1
            # PMs
            if row == 6 and column == 4:
                charGrid.controls.extend(
                    [
                        letter(
                            charRow[column],
                            active=True
                        ),
                        letter(
                            charRow[column + 1],
                            active=True
                        )
                    ]
                )
                column += 1

    return charGrid
