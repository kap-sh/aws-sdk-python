"""Generated from Smithy shape ``com.amazonaws.dynamodb#NumberSetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.number_attribute_value

NumberSetAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.number_attribute_value.NumberAttributeValue"
]
