"""Generated from Smithy shape ``com.amazonaws.support#SupportedHour``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.end_time
    import aws_sdk_support.types.start_time


class SupportedHour(TypedDict):
    start_time: NotRequired["aws_sdk_support.types.start_time.StartTime"]
    """<p> Start Time. RFC 3339 format <code>'HH:mm:ss.SSS'</code>. </p>"""
    end_time: NotRequired["aws_sdk_support.types.end_time.EndTime"]
    """<p> End Time. RFC 3339 format <code>'HH:mm:ss.SSS'</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedHour) -> dict:
    out: dict = {}
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedHour:
    out: SupportedHour = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    return out
