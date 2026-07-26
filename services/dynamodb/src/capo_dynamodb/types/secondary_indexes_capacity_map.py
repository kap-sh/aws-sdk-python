"""Generated from Smithy shape ``com.amazonaws.dynamodb#SecondaryIndexesCapacityMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.capacity
    import capo_dynamodb.types.index_name

SecondaryIndexesCapacityMap: TypeAlias = dict[
    "capo_dynamodb.types.index_name.IndexName", "capo_dynamodb.types.capacity.Capacity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: SecondaryIndexesCapacityMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.capacity

        out[key] = capo_dynamodb.types.capacity.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> SecondaryIndexesCapacityMap:
    out: SecondaryIndexesCapacityMap = {}
    for key, value in data.items():
        import capo_dynamodb.types.capacity

        out[key] = capo_dynamodb.types.capacity.deserialize_aws_json_1_0(value)
    return out
