"""Generated from Smithy shape ``com.amazonaws.pinpoint#QuietTime``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class QuietTime(TypedDict):
    end: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The specific time when quiet time ends. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.</p>"""
    start: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The specific time when quiet time begins. This value has to use 24-hour notation and be in HH:MM format, where HH is the hour (with a leading zero, if applicable) and MM is the minutes. For example, use 02:30 to represent 2:30 AM, or 14:30 to represent 2:30 PM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuietTime) -> dict:
    out: dict = {}
    if "end" in value:
        out["End"] = value["end"]
    if "start" in value:
        out["Start"] = value["start"]
    return out


def deserialize_json(data: dict) -> QuietTime:
    out: QuietTime = {}  # type: ignore[typeddict-item]
    if "End" in data:
        out["end"] = data["End"]
    if "Start" in data:
        out["start"] = data["Start"]
    return out
