#!/usr/bin/env python
"""Generate a calendar for Leia's immunotherapy schedule for Golden Gate Veterinary Specialists."""
__author__ = "David Sielert"
__license__ = "MIT"
__version__ = "0.1.0"

import datetime
from ical.calendar import Calendar
from ical.event import Event
from pathlib import Path
from ical.calendar_stream import IcsCalendarStream


cal = Calendar()
schedule_days = {
    1: {"Vial": 1, "Dose": "0.1cc", "Comment": "Initial Dose"},
    3: {"Vial": 1, "Dose": "0.2cc", "Comment": "Titrate Dose"},
    5: {"Vial": 1, "Dose": "0.4cc", "Comment": "Titrate Dose"},
    7: {"Vial": 1, "Dose": "0.8cc", "Comment": "Titrate Dose"},
    9: {"Vial": 1, "Dose": "1.0cc", "Comment": "Titrate Dose"},
    11: {"Vial": 2, "Dose": "0.1cc", "Comment": "Titrate Dose"},
    13: {"Vial": 2, "Dose": "0.2cc", "Comment": "Titrate Dose"},
    15: {"Vial": 2, "Dose": "0.4cc", "Comment": "Titrate Dose"},
    17: {"Vial": 2, "Dose": "0.8cc", "Comment": "Titrate Dose"},
    19: {"Vial": 2, "Dose": "1.0cc", "Comment": "Titrate Dose"},
    21: {"Vial": 3, "Dose": "0.1cc", "Comment": "Titrate Dose"},
    23: {"Vial": 3, "Dose": "0.2cc", "Comment": "Titrate Dose"},
    25: {"Vial": 3, "Dose": "0.4cc", "Comment": "Titrate Dose"},
    27: {"Vial": 3, "Dose": "0.8cc", "Comment": "Titrate Dose"},
    29: {"Vial": 3, "Dose": "1.0cc", "Comment": "Titrate Dose"},
    36: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #1"},
    43: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #2"},
    50: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #3"},
    57: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #4"},
    64: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #5"},
    71: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #6"},
    78: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #7"},
    85: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #8"},
    92: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #9"},
    99: {"Vial": 3, "Dose": "1.0cc", "Comment": "Maintenance Dose WK #10"},
}

start = datetime.date.today()
res_date = start
for i in range(1, 100):
    if i in schedule_days:
        res_date += datetime.timedelta(days=i)
        item = schedule_days[i]
        summary = f"Leia Immunotherapy Day {i}"
        description = f"""
Vial: {item["Vial"]}
Dose: {item["Dose"]}
Comment: {item["Comment"]}
"""
        # print("-----")
        # print(title, res_date.strftime("%m/%d/%Y"))
        # print(description)
        cal.events.append(
            Event(summary=summary, start=res_date, description=description),
        )
    res_date += datetime.timedelta(days=1)


filename = Path("leia.ics")
with filename.open(mode="w") as ics_file:
    ics_file.write(IcsCalendarStream.calendar_to_ics(cal))
