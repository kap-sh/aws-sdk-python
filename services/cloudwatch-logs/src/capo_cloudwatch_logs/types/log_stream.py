"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.log_stream_name
    import capo_cloudwatch_logs.types.sequence_token
    import capo_cloudwatch_logs.types.stored_bytes
    import capo_cloudwatch_logs.types.timestamp


class LogStream(TypedDict, closed=True):
    log_stream_name: NotRequired[
        "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>The name of the log stream.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the stream, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    first_event_timestamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time of the first event, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    last_event_timestamp: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. The <code>lastEventTime</code> value updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.</p>"""
    last_ingestion_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The ingestion time, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code> The <code>lastIngestionTime</code> value updates on an eventual consistency basis. It typically updates in less than an hour after ingestion, but in rare situations might take longer.</p>"""
    upload_sequence_token: NotRequired[
        "capo_cloudwatch_logs.types.sequence_token.SequenceToken"
    ]
    """<p>The sequence token.</p> <important> <p>The sequence token is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are always accepted regardless of receiving an invalid sequence token. You don't need to obtain <code>uploadSequenceToken</code> to use a <code>PutLogEvents</code> action.</p> </important>"""
    arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the log stream.</p>"""
    stored_bytes: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The number of bytes stored.</p> <p> <b>Important:</b> As of June 17, 2019, this parameter is no longer supported for log streams, and is always reported as zero. This change applies only to log streams. The <code>storedBytes</code> parameter for log groups is not affected.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogStream) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "first_event_timestamp" in value:
        out["firstEventTimestamp"] = value["first_event_timestamp"]
    if "last_event_timestamp" in value:
        out["lastEventTimestamp"] = value["last_event_timestamp"]
    if "last_ingestion_time" in value:
        out["lastIngestionTime"] = value["last_ingestion_time"]
    if "upload_sequence_token" in value:
        out["uploadSequenceToken"] = value["upload_sequence_token"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "stored_bytes" in value:
        out["storedBytes"] = value["stored_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogStream:
    out: LogStream = {}  # type: ignore[typeddict-item]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "firstEventTimestamp" in data:
        out["first_event_timestamp"] = data["firstEventTimestamp"]
    if "lastEventTimestamp" in data:
        out["last_event_timestamp"] = data["lastEventTimestamp"]
    if "lastIngestionTime" in data:
        out["last_ingestion_time"] = data["lastIngestionTime"]
    if "uploadSequenceToken" in data:
        out["upload_sequence_token"] = data["uploadSequenceToken"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "storedBytes" in data:
        out["stored_bytes"] = data["storedBytes"]
    return out
