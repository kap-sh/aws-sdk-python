"""Generated from Smithy shape ``com.amazonaws.mq#WeeklyStartTime``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.day_of_week


class WeeklyStartTime(TypedDict, closed=True):
    day_of_week: NotRequired["aws_sdk_mq.types.day_of_week.DayOfWeek"]
    """<p>Required. The day of the week.</p>"""
    time_of_day: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>Required. The time, in 24-hour format.</p>"""
    time_zone: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The time zone, UTC by default, in either the Country/City format, or the UTC offset format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklyStartTime) -> dict:
    out: dict = {}
    if "day_of_week" in value:
        import aws_sdk_mq.types.day_of_week

        out["dayOfWeek"] = aws_sdk_mq.types.day_of_week.serialize_json(
            value["day_of_week"]
        )
    if "time_of_day" in value:
        out["timeOfDay"] = value["time_of_day"]
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> WeeklyStartTime:
    out: WeeklyStartTime = {}  # type: ignore[typeddict-item]
    if "dayOfWeek" in data:
        import aws_sdk_mq.types.day_of_week

        out["day_of_week"] = aws_sdk_mq.types.day_of_week.deserialize_json(
            data["dayOfWeek"]
        )
    if "timeOfDay" in data:
        out["time_of_day"] = data["timeOfDay"]
    if "timeZone" in data:
        out["time_zone"] = data["timeZone"]
    return out
