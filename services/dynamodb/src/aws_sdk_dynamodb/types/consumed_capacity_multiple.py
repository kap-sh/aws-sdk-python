"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConsumedCapacityMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.consumed_capacity

ConsumedCapacityMultiple: TypeAlias = list[
    "aws_sdk_dynamodb.types.consumed_capacity.ConsumedCapacity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConsumedCapacityMultiple) -> list:
    import aws_sdk_dynamodb.types.consumed_capacity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConsumedCapacityMultiple:
    import aws_sdk_dynamodb.types.consumed_capacity

    out: ConsumedCapacityMultiple = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(item)
        )
    return out
