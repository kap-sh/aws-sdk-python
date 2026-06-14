"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLogStreamsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.descending
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.order_by


class DescribeLogStreamsRequest(TypedDict):
    log_group_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>Specify either the name or ARN of the log group to view. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>The prefix to match.</p> <p>If <code>orderBy</code> is <code>LastEventTime</code>, you cannot specify this parameter.</p>"""
    order_by: NotRequired["aws_sdk_cloudwatch_logs.types.order_by.OrderBy"]
    """<p>If the value is <code>LogStreamName</code>, the results are ordered by log stream name. If the value is <code>LastEventTime</code>, the results are ordered by the event time. The default value is <code>LogStreamName</code>.</p> <p>If you order the results by event time, you cannot specify the <code>logStreamNamePrefix</code> parameter.</p> <p> <code>lastEventTimestamp</code> represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. <code>lastEventTimestamp</code> updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.</p>"""
    descending: NotRequired["aws_sdk_cloudwatch_logs.types.descending.Descending"]
    """<p>If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogStreamsRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "order_by" in value:
        import aws_sdk_cloudwatch_logs.types.order_by

        out["orderBy"] = aws_sdk_cloudwatch_logs.types.order_by.serialize_aws_json_1_1(
            value["order_by"]
        )
    if "descending" in value:
        out["descending"] = value["descending"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogStreamsRequest:
    out: DescribeLogStreamsRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    if "orderBy" in data:
        import aws_sdk_cloudwatch_logs.types.order_by

        out["order_by"] = (
            aws_sdk_cloudwatch_logs.types.order_by.deserialize_aws_json_1_1(
                data["orderBy"]
            )
        )
    if "descending" in data:
        out["descending"] = data["descending"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
