"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpressionAttributeNameMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_name_variable
    import aws_sdk_dynamodb.types.attribute_name

ExpressionAttributeNameMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.expression_attribute_name_variable.ExpressionAttributeNameVariable",
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ExpressionAttributeNameMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpressionAttributeNameMap:
    out: ExpressionAttributeNameMap = {}
    for key, value in data.items():
        out[key] = value
    return out
