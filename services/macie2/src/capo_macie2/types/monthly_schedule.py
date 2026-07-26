"""Generated from Smithy shape ``com.amazonaws.macie2#MonthlySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__integer


class MonthlySchedule(TypedDict, closed=True):
    day_of_month: NotRequired["capo_macie2.types.__integer.__integer"]
    """<p>The numeric day of the month when Amazon Macie runs the job. This value can be an integer from 1 through 31.</p> <p>If this value exceeds the number of days in a certain month, Macie doesn't run the job that month. Macie runs the job only during months that have the specified day. For example, if this value is 31 and a month has only 30 days, Macie doesn't run the job that month. To run the job every month, specify a value that's less than 29.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonthlySchedule) -> dict:
    out: dict = {}
    if "day_of_month" in value:
        out["dayOfMonth"] = value["day_of_month"]
    return out


def deserialize_json(data: dict) -> MonthlySchedule:
    out: MonthlySchedule = {}  # type: ignore[typeddict-item]
    if "dayOfMonth" in data:
        out["day_of_month"] = data["dayOfMonth"]
    return out
