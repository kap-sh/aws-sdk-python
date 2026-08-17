"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeLogStreamsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_streams
    import capo_cloudwatch_logs.types.next_token


class DescribeLogStreamsResponse(TypedDict, closed=True):
    log_streams: NotRequired["capo_cloudwatch_logs.types.log_streams.LogStreams"]
    """<p>The log streams.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLogStreamsResponse) -> dict:
    out: dict = {}
    if "log_streams" in value:
        import capo_cloudwatch_logs.types.log_streams

        out["logStreams"] = (
            capo_cloudwatch_logs.types.log_streams.serialize_aws_json_1_1(
                value["log_streams"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLogStreamsResponse:
    out: DescribeLogStreamsResponse = {}  # type: ignore[typeddict-item]
    if data.get("logStreams") is not None:
        import capo_cloudwatch_logs.types.log_streams

        out["log_streams"] = (
            capo_cloudwatch_logs.types.log_streams.deserialize_aws_json_1_1(
                data["logStreams"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
