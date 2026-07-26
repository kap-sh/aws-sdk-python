"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpressionAttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_value
    import capo_dynamodb.types.expression_attribute_value_variable

ExpressionAttributeValueMap: TypeAlias = dict[
    "capo_dynamodb.types.expression_attribute_value_variable.ExpressionAttributeValueVariable",
    "capo_dynamodb.types.attribute_value.AttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ExpressionAttributeValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.attribute_value

        out[key] = capo_dynamodb.types.attribute_value.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpressionAttributeValueMap:
    out: ExpressionAttributeValueMap = {}
    for key, value in data.items():
        import capo_dynamodb.types.attribute_value

        out[key] = capo_dynamodb.types.attribute_value.deserialize_aws_json_1_0(value)
    return out
