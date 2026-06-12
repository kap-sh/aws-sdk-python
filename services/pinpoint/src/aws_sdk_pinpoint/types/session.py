"""Generated from Smithy shape ``com.amazonaws.pinpoint#Session``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string


class Session(TypedDict):
    duration: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>The duration of the session, in milliseconds.</p>"""
    id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the session.</p>"""
    start_timestamp: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time when the session began.</p>"""
    stop_timestamp: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time when the session ended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Session) -> dict:
    out: dict = {}
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "id" in value:
        out["Id"] = value["id"]
    if "start_timestamp" in value:
        out["StartTimestamp"] = value["start_timestamp"]
    if "stop_timestamp" in value:
        out["StopTimestamp"] = value["stop_timestamp"]
    return out


def deserialize_json(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "StartTimestamp" in data:
        out["start_timestamp"] = data["StartTimestamp"]
    if "StopTimestamp" in data:
        out["stop_timestamp"] = data["StopTimestamp"]
    return out
