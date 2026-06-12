"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_source

DeliverySources: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.delivery_source.DeliverySource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySources) -> list:
    import aws_sdk_cloudwatch_logs.types.delivery_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliverySources:
    import aws_sdk_cloudwatch_logs.types.delivery_source

    out: DeliverySources = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.delivery_source.deserialize_aws_json_1_1(item)
        )
    return out
