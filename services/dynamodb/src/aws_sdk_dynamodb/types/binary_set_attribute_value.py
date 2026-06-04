"""Generated from Smithy shape ``com.amazonaws.dynamodb#BinarySetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.binary_attribute_value

BinarySetAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.binary_attribute_value.BinaryAttributeValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BinarySetAttributeValue) -> list:
    import aws_sdk_dynamodb.types.binary_attribute_value

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dynamodb.types.binary_attribute_value.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BinarySetAttributeValue:
    import aws_sdk_dynamodb.types.binary_attribute_value

    out: BinarySetAttributeValue = []
    for item in data:
        out.append(
            aws_sdk_dynamodb.types.binary_attribute_value.deserialize_aws_json_1_0(item)
        )
    return out
