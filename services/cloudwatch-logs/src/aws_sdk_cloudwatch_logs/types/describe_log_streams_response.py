"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLogStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_streams
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeLogStreamsResponse(TypedDict, closed=True):
    log_streams: NotRequired["aws_sdk_cloudwatch_logs.types.log_streams.LogStreams"]
    """<p>The log streams.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogStreamsResponse) -> dict:
    out: dict = {}
    if "log_streams" in value:
        import aws_sdk_cloudwatch_logs.types.log_streams

        out["logStreams"] = (
            aws_sdk_cloudwatch_logs.types.log_streams.serialize_aws_json_1_1(
                value["log_streams"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogStreamsResponse:
    out: DescribeLogStreamsResponse = {}  # type: ignore[typeddict-item]
    if "logStreams" in data:
        import aws_sdk_cloudwatch_logs.types.log_streams

        out["log_streams"] = (
            aws_sdk_cloudwatch_logs.types.log_streams.deserialize_aws_json_1_1(
                data["logStreams"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
