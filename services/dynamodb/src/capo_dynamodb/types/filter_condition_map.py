"""Generated from Smithy shape ``com.amazonaws.dynamodb#FilterConditionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name
    import capo_dynamodb.types.condition

FilterConditionMap: TypeAlias = dict[
    "capo_dynamodb.types.attribute_name.AttributeName",
    "capo_dynamodb.types.condition.Condition",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: FilterConditionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.condition

        out[key] = capo_dynamodb.types.condition.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> FilterConditionMap:
    out: FilterConditionMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.condition

        out[key] = capo_dynamodb.types.condition.deserialize_aws_json_1_0(value)
    return out
