"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeliverySources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source

DeliverySources: TypeAlias = list[
    "capo_cloudwatch_logs.types.delivery_source.DeliverySource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliverySources) -> list:
    import capo_cloudwatch_logs.types.delivery_source

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.delivery_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeliverySources:
    import capo_cloudwatch_logs.types.delivery_source

    out: DeliverySources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.delivery_source.deserialize_aws_json_1_1(item)
        )
    return out
