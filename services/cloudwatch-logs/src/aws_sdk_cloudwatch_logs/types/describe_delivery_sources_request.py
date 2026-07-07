"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliverySourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeDeliverySourcesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of delivery sources to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliverySourcesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliverySourcesRequest:
    out: DescribeDeliverySourcesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
