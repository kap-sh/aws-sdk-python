"""Generated from Smithy shape ``com.amazonaws.inspector2#WeeklySchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.days_list
    import aws_sdk_inspector2.types.time


class WeeklySchedule(TypedDict):
    start_time: "aws_sdk_inspector2.types.time.Time"
    """<p>The weekly schedule's start time.</p>"""
    days: "aws_sdk_inspector2.types.days_list.DaysList"
    """<p>The weekly schedule's days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeeklySchedule) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.time

    out["startTime"] = aws_sdk_inspector2.types.time.serialize_json(value["start_time"])
    import aws_sdk_inspector2.types.days_list

    out["days"] = aws_sdk_inspector2.types.days_list.serialize_json(value["days"])
    return out


def deserialize_json(data: dict) -> WeeklySchedule:
    out: WeeklySchedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_inspector2.types.time

        out["start_time"] = aws_sdk_inspector2.types.time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("WeeklySchedule.start_time required")
    if "days" in data:
        import aws_sdk_inspector2.types.days_list

        out["days"] = aws_sdk_inspector2.types.days_list.deserialize_json(data["days"])
    else:
        raise DeserializationError("WeeklySchedule.days required")
    return out
