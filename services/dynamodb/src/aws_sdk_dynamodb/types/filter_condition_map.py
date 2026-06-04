"""Generated from Smithy shape ``com.amazonaws.dynamodb#FilterConditionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name
    import aws_sdk_dynamodb.types.condition

FilterConditionMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb.types.condition.Condition",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: FilterConditionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.condition

        out[key] = aws_sdk_dynamodb.types.condition.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> FilterConditionMap:
    out: FilterConditionMap = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.condition

        out[key] = aws_sdk_dynamodb.types.condition.deserialize_aws_json_1_0(value)
    return out
