"""Generated from Smithy shape ``com.amazonaws.macie2#WeeklySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.day_of_week


class WeeklySchedule(TypedDict, closed=True):
    day_of_week: NotRequired["capo_macie2.types.day_of_week.DayOfWeek"]
    """<p>The day of the week when Amazon Macie runs the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklySchedule) -> dict:
    out: dict = {}
    if "day_of_week" in value:
        import capo_macie2.types.day_of_week

        out["dayOfWeek"] = capo_macie2.types.day_of_week.serialize_json(
            value["day_of_week"]
        )
    return out


def deserialize_json(data: dict) -> WeeklySchedule:
    out: WeeklySchedule = {}  # type: ignore[typeddict-item]
    if "dayOfWeek" in data:
        import capo_macie2.types.day_of_week

        out["day_of_week"] = capo_macie2.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    return out
