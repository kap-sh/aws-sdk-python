"""Generated from Smithy shape ``com.amazonaws.dynamodb#BinarySetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.binary_attribute_value

BinarySetAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.binary_attribute_value.BinaryAttributeValue"
]
