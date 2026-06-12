"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliveryDestinationTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type

DeliveryDestinationTypes: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryDestinationTypes) -> list:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliveryDestinationTypes:
    import aws_sdk_cloudwatch_logs.types.delivery_destination_type

    out: DeliveryDestinationTypes = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_destination_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
