"""Generated from Smithy shape ``com.amazonaws.pinpoint#OpenHoursRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class OpenHoursRule(TypedDict, closed=True):
    start_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The start of the scheduled time, in ISO 8601 format, when the channel can send messages.</p>"""
    end_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The end of the scheduled time, in ISO 8601 format, when the channel can't send messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenHoursRule) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["StartTime"] = value["start_time"]
    if "end_time" in value:
        out["EndTime"] = value["end_time"]
    return out


def deserialize_json(data: dict) -> OpenHoursRule:
    out: OpenHoursRule = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    return out
