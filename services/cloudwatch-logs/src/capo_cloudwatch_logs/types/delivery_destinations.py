"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination

DeliveryDestinations: TypeAlias = list[
    "capo_cloudwatch_logs.types.delivery_destination.DeliveryDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestinations) -> list:
    import capo_cloudwatch_logs.types.delivery_destination

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.delivery_destination.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliveryDestinations:
    import capo_cloudwatch_logs.types.delivery_destination

    out: DeliveryDestinations = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.delivery_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out
