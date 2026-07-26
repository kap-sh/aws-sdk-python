"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FilteredLogEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.event_id
    import capo_cloudwatch_logs.types.event_message
    import capo_cloudwatch_logs.types.log_stream_name
    import capo_cloudwatch_logs.types.timestamp


class FilteredLogEvent(TypedDict, closed=True):
    log_stream_name: NotRequired[
        "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>The name of the log stream to which this event belongs.</p>"""
    timestamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    message: NotRequired["capo_cloudwatch_logs.types.event_message.EventMessage"]
    """<p>The data contained in the log event.</p>"""
    ingestion_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time the event was ingested, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    event_id: NotRequired["capo_cloudwatch_logs.types.event_id.EventId"]
    """<p>The ID of the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilteredLogEvent) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "message" in value:
        out["message"] = value["message"]
    if "ingestion_time" in value:
        out["ingestionTime"] = value["ingestion_time"]
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilteredLogEvent:
    out: FilteredLogEvent = {}  # type: ignore[typeddict-item]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "message" in data:
        out["message"] = data["message"]
    if "ingestionTime" in data:
        out["ingestion_time"] = data["ingestionTime"]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    return out
