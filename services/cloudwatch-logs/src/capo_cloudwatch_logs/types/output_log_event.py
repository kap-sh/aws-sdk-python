"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OutputLogEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.event_message
    import capo_cloudwatch_logs.types.timestamp


class OutputLogEvent(TypedDict, closed=True):
    timestamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    message: NotRequired["capo_cloudwatch_logs.types.event_message.EventMessage"]
    """<p>The data contained in the log event.</p>"""
    ingestion_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time the event was ingested, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputLogEvent) -> dict:
    out: dict = {}
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "message" in value:
        out["message"] = value["message"]
    if "ingestion_time" in value:
        out["ingestionTime"] = value["ingestion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputLogEvent:
    out: OutputLogEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "message" in data:
        out["message"] = data["message"]
    if "ingestionTime" in data:
        out["ingestion_time"] = data["ingestionTime"]
    return out
