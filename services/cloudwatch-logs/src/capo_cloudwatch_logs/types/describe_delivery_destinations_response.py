"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveryDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destinations
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliveryDestinationsResponse(TypedDict, closed=True):
    delivery_destinations: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destinations.DeliveryDestinations"
    ]
    """<p>An array of structures. Each structure contains information about one delivery destination in the account.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryDestinationsResponse) -> dict:
    out: dict = {}
    if "delivery_destinations" in value:
        import capo_cloudwatch_logs.types.delivery_destinations

        out["deliveryDestinations"] = (
            capo_cloudwatch_logs.types.delivery_destinations.serialize_aws_json_1_1(
                value["delivery_destinations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryDestinationsResponse:
    out: DescribeDeliveryDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "deliveryDestinations" in data:
        import capo_cloudwatch_logs.types.delivery_destinations

        out["delivery_destinations"] = (
            capo_cloudwatch_logs.types.delivery_destinations.deserialize_aws_json_1_1(
                data["deliveryDestinations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
