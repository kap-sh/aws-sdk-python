"""Generated from Smithy shape ``com.amazonaws.quicksight#ScheduleRefreshOnEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.day_of_month
    import aws_sdk_quicksight.types.day_of_week


class ScheduleRefreshOnEntity(TypedDict, closed=True):
    day_of_week: NotRequired["aws_sdk_quicksight.types.day_of_week.DayOfWeek"]
    """<p>The day of the week that you want to schedule a refresh on.</p>"""
    day_of_month: NotRequired["aws_sdk_quicksight.types.day_of_month.DayOfMonth"]
    """<p>The day of the month that you want to schedule refresh on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleRefreshOnEntity) -> dict:
    out: dict = {}
    if "day_of_week" in value:
        import aws_sdk_quicksight.types.day_of_week

        out["DayOfWeek"] = aws_sdk_quicksight.types.day_of_week.serialize_json(
            value["day_of_week"]
        )
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    return out


def deserialize_json(data: dict) -> ScheduleRefreshOnEntity:
    out: ScheduleRefreshOnEntity = {}  # type: ignore[typeddict-item]
    if "DayOfWeek" in data:
        import aws_sdk_quicksight.types.day_of_week

        out["day_of_week"] = aws_sdk_quicksight.types.day_of_week.deserialize_json(
            data["DayOfWeek"]
        )
    if "DayOfMonth" in data:
        out["day_of_month"] = data["DayOfMonth"]
    return out
