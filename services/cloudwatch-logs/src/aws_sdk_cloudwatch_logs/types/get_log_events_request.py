"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.events_limit
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.start_from_head
    import aws_sdk_cloudwatch_logs.types.timestamp
    import aws_sdk_cloudwatch_logs.types.unmask


class GetLogEventsRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>Specify either the name or ARN of the log group to view events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_stream_name: "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    """<p>The name of the log stream.</p>"""
    start_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp equal to this time or later than this time are included. Events with a timestamp earlier than this time are not included.</p>"""
    end_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp equal to or later than this time are not included.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.events_limit.EventsLimit"]
    """<p>The maximum number of log events returned. If you don't specify a limit, the default is as many log events as can fit in a response size of 1 MB (up to 10,000 log events).</p>"""
    start_from_head: NotRequired[
        "aws_sdk_cloudwatch_logs.types.start_from_head.StartFromHead"
    ]
    """<p>If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.</p> <p>If you are using a previous <code>nextForwardToken</code> value as the <code>nextToken</code> in this operation, you must specify <code>true</code> for <code>startFromHead</code>.</p>"""
    unmask: "aws_sdk_cloudwatch_logs.types.unmask.Unmask"
    """<p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogEventsRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    out["logStreamName"] = value["log_stream_name"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "start_from_head" in value:
        out["startFromHead"] = value["start_from_head"]
    out["unmask"] = value.get("unmask", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogEventsRequest:
    out: GetLogEventsRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    else:
        raise DeserializationError("GetLogEventsRequest.log_stream_name required")
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "startFromHead" in data:
        out["start_from_head"] = data["startFromHead"]
    if "unmask" in data:
        out["unmask"] = data["unmask"]
    else:
        out["unmask"] = False
    return out
