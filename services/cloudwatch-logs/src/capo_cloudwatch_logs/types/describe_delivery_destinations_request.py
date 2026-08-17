"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveryDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliveryDestinationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of delivery destinations to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryDestinationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryDestinationsRequest:
    out: DescribeDeliveryDestinationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    return out
