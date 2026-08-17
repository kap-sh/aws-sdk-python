"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.timestamp


class ImportFilter(TypedDict, closed=True):
    start_event_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start of the time range for events to import, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    end_event_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
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
    if data.get("startEventTime") is not None:
        out["start_event_time"] = data["startEventTime"]
    if data.get("endEventTime") is not None:
        out["end_event_time"] = data["endEventTime"]
    return out
