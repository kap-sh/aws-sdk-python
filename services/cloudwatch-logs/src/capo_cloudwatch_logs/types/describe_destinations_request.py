"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.destination_name
    import capo_cloudwatch_logs.types.next_token


class DescribeDestinationsRequest(TypedDict, closed=True):
    destination_name_prefix: NotRequired[
        "capo_cloudwatch_logs.types.destination_name.DestinationName"
    ]
    """<p>The prefix to match. If you don't specify a value, no prefix filter is applied.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default maximum value of 50 items is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDestinationsRequest) -> dict:
    out: dict = {}
    if "destination_name_prefix" in value:
        out["DestinationNamePrefix"] = value["destination_name_prefix"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDestinationsRequest:
    out: DescribeDestinationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DestinationNamePrefix") is not None:
        out["destination_name_prefix"] = data["DestinationNamePrefix"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
