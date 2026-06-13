"""Generated from Smithy shape ``com.amazonaws.inspector2#DailySchedule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.time


class DailySchedule(TypedDict):
    start_time: "aws_sdk_inspector2.types.time.Time"
    """<p>The schedule start time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DailySchedule) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.time

    out["startTime"] = aws_sdk_inspector2.types.time.serialize_json(value["start_time"])
    return out


def deserialize_json(data: dict) -> DailySchedule:
    out: DailySchedule = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import aws_sdk_inspector2.types.time

        out["start_time"] = aws_sdk_inspector2.types.time.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError("DailySchedule.start_time required")
    return out
