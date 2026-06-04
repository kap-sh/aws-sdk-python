"""Generated from Smithy shape ``com.amazonaws.dynamodb#NumberSetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.number_attribute_value

NumberSetAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.number_attribute_value.NumberAttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NumberSetAttributeValue) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NumberSetAttributeValue:
    return list(data)
