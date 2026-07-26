"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destinations
    import capo_cloudwatch_logs.types.next_token


class DescribeDestinationsResponse(TypedDict, closed=True):
    destinations: NotRequired["capo_cloudwatch_logs.types.destinations.Destinations"]
    """<p>The destinations.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDestinationsResponse) -> dict:
    out: dict = {}
    if "destinations" in value:
        import capo_cloudwatch_logs.types.destinations

        out["destinations"] = (
            capo_cloudwatch_logs.types.destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDestinationsResponse:
    out: DescribeDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "destinations" in data:
        import capo_cloudwatch_logs.types.destinations

        out["destinations"] = (
            capo_cloudwatch_logs.types.destinations.deserialize_aws_json_1_1(
                data["destinations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
