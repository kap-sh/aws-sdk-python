"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Deliveries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery

Deliveries: TypeAlias = list["capo_cloudwatch_logs.types.delivery.Delivery"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Deliveries) -> list:
    import capo_cloudwatch_logs.types.delivery

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.delivery.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Deliveries:
    import capo_cloudwatch_logs.types.delivery

    out: Deliveries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch_logs.types.delivery.deserialize_aws_json_1_1(item))
    return out
