"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveryDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destinations
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeDeliveryDestinationsResponse(TypedDict):
    delivery_destinations: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_destinations.DeliveryDestinations"
    ]
    """<p>An array of structures. Each structure contains information about one delivery destination in the account.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryDestinationsResponse) -> dict:
    out: dict = {}
    if "delivery_destinations" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_destinations

        out["deliveryDestinations"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destinations.serialize_aws_json_1_1(
                value["delivery_destinations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryDestinationsResponse:
    out: DescribeDeliveryDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "deliveryDestinations" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_destinations

        out["delivery_destinations"] = (
            aws_sdk_cloudwatch_logs.types.delivery_destinations.deserialize_aws_json_1_1(
                data["deliveryDestinations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
