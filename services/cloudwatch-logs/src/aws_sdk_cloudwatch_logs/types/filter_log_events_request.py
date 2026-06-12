"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FilterLogEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.events_limit
    import aws_sdk_cloudwatch_logs.types.filter_pattern
    import aws_sdk_cloudwatch_logs.types.input_log_stream_names
    import aws_sdk_cloudwatch_logs.types.interleaved
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.timestamp
    import aws_sdk_cloudwatch_logs.types.unmask


class FilterLogEventsRequest(TypedDict):
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group to search.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>Specify either the name or ARN of the log group to view log events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_stream_names: NotRequired[
        "aws_sdk_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
    ]
    """<p>Filters the results to only logs from the log streams in this list.</p> <p>If you specify a value for both <code>logStreamNames</code> and <code>logStreamNamePrefix</code>, the action returns an <code>InvalidParameterException</code> error.</p>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>Filters the results to include only events from log streams that have names starting with this prefix.</p> <p>If you specify a value for both <code>logStreamNamePrefix</code> and <code>logStreamNames</code>, the action returns an <code>InvalidParameterException</code> error.</p>"""
    start_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The start of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp before this time are not returned.</p>"""
    end_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The end of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp later than this time are not returned.</p>"""
    filter_pattern: NotRequired[
        "aws_sdk_cloudwatch_logs.types.filter_pattern.FilterPattern"
    ]
    """<p>The filter pattern to use. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html\">Filter and Pattern Syntax</a>.</p> <p>If not provided, all the events are matched.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of events to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.events_limit.EventsLimit"]
    """<p>The maximum number of events to return. The default is 10,000 events.</p>"""
    interleaved: NotRequired["aws_sdk_cloudwatch_logs.types.interleaved.Interleaved"]
    """<p>If the value is true, the operation attempts to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on.</p> <p> <b>Important</b> As of June 17, 2019, this parameter is ignored and the value is assumed to be true. The response from this operation always interleaves events from multiple log streams within a log group.</p>"""
    unmask: "aws_sdk_cloudwatch_logs.types.unmask.Unmask"
    """<p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterLogEventsRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "log_stream_names" in value:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["logStreamNames"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.serialize_aws_json_1_1(
                value["log_stream_names"]
            )
        )
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "filter_pattern" in value:
        out["filterPattern"] = value["filter_pattern"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "interleaved" in value:
        out["interleaved"] = value["interleaved"]
    out["unmask"] = value.get("unmask", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterLogEventsRequest:
    out: FilterLogEventsRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "logStreamNames" in data:
        import aws_sdk_cloudwatch_logs.types.input_log_stream_names

        out["log_stream_names"] = (
            aws_sdk_cloudwatch_logs.types.input_log_stream_names.deserialize_aws_json_1_1(
                data["logStreamNames"]
            )
        )
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "filterPattern" in data:
        out["filter_pattern"] = data["filterPattern"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "interleaved" in data:
        out["interleaved"] = data["interleaved"]
    if "unmask" in data:
        out["unmask"] = data["unmask"]
    else:
        out["unmask"] = False
    return out
