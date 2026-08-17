"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConsumedCapacityMultiple``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity

ConsumedCapacityMultiple: TypeAlias = list[
    "capo_dynamodb.types.consumed_capacity.ConsumedCapacity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConsumedCapacityMultiple) -> list:
    import capo_dynamodb.types.consumed_capacity

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ConsumedCapacityMultiple:
    import capo_dynamodb.types.consumed_capacity

    out: ConsumedCapacityMultiple = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(item))
    return out
