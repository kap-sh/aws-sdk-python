"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpressionAttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_value_variable
    import aws_sdk_dynamodb.types.attribute_value

ExpressionAttributeValueMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.expression_attribute_value_variable.ExpressionAttributeValueVariable",
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ExpressionAttributeValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_dynamodb.types.attribute_value

        out[key] = aws_sdk_dynamodb.types.attribute_value.serialize_aws_json_1_0(value)
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpressionAttributeValueMap:
    out: ExpressionAttributeValueMap = {}
    for key, value in data.items():
        import aws_sdk_dynamodb.types.attribute_value

        out[key] = aws_sdk_dynamodb.types.attribute_value.deserialize_aws_json_1_0(
            value
        )
    return out
