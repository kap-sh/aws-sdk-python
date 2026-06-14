"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.timestamp


class ImportFilter(TypedDict):
    start_event_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start of the time range for events to import, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    end_event_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end of the time range for events to import, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFilter) -> dict:
    out: dict = {}
    if "start_event_time" in value:
        out["startEventTime"] = value["start_event_time"]
    if "end_event_time" in value:
        out["endEventTime"] = value["end_event_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportFilter:
    out: ImportFilter = {}  # type: ignore[typeddict-item]
    if "startEventTime" in data:
        out["start_event_time"] = data["startEventTime"]
    if "endEventTime" in data:
        out["end_event_time"] = data["endEventTime"]
    return out
