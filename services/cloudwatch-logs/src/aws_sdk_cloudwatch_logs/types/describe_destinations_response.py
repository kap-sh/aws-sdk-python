"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destinations
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeDestinationsResponse(TypedDict):
    destinations: NotRequired["aws_sdk_cloudwatch_logs.types.destinations.Destinations"]
    """<p>The destinations.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDestinationsResponse) -> dict:
    out: dict = {}
    if "destinations" in value:
        import aws_sdk_cloudwatch_logs.types.destinations

        out["destinations"] = (
            aws_sdk_cloudwatch_logs.types.destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDestinationsResponse:
    out: DescribeDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import aws_sdk_cloudwatch_logs.types.destinations

        out["destinations"] = (
            aws_sdk_cloudwatch_logs.types.destinations.deserialize_aws_json_1_1(
                data["destinations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
