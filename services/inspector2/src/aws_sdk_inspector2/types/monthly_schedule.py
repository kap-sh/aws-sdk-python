"""Generated from Smithy shape ``com.amazonaws.inspector2#MonthlySchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.day
    import aws_sdk_inspector2.types.time


class MonthlySchedule(TypedDict):
    start_time: "aws_sdk_inspector2.types.time.Time"
    """<p>The monthly schedule's start time.</p>"""
    day: "aws_sdk_inspector2.types.day.Day"
    """<p>The monthly schedule's day.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonthlySchedule) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.time

    out["startTime"] = aws_sdk_inspector2.types.time.serialize_json(value["start_time"])
    import aws_sdk_inspector2.types.day

    out["day"] = aws_sdk_inspector2.types.day.serialize_json(value["day"])
    return out


def deserialize_json(data: dict) -> MonthlySchedule:
    out: MonthlySchedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_inspector2.types.time

        out["start_time"] = aws_sdk_inspector2.types.time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("MonthlySchedule.start_time required")
    if "day" in data:
        import aws_sdk_inspector2.types.day

        out["day"] = aws_sdk_inspector2.types.day.deserialize_json(data["day"])
    else:
        raise DeserializationError("MonthlySchedule.day required")
    return out
