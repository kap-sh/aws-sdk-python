"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveriesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.describe_limit
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeDeliveriesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["aws_sdk_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of deliveries to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveriesRequest:
    out: DescribeDeliveriesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    return out
