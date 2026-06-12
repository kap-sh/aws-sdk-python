"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LiveTailSessionLogEvent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_message
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.timestamp


class LiveTailSessionLogEvent(TypedDict):
    log_stream_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>The name of the log stream that ingested this log event.</p>"""
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The name or ARN of the log group that ingested this log event.</p>"""
    message: NotRequired["aws_sdk_cloudwatch_logs.types.event_message.EventMessage"]
    """<p>The log event message text.</p>"""
    timestamp: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp specifying when this log event was created.</p>"""
    ingestion_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp specifying when this log event was ingested into the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LiveTailSessionLogEvent) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "message" in value:
        out["message"] = value["message"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "ingestion_time" in value:
        out["ingestionTime"] = value["ingestion_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LiveTailSessionLogEvent:
    out: LiveTailSessionLogEvent = {}  # type: ignore[typeddict-item]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "message" in data:
        out["message"] = data["message"]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "ingestionTime" in data:
        out["ingestion_time"] = data["ingestionTime"]
    return out
