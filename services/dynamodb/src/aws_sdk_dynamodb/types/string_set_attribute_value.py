"""Generated from Smithy shape ``com.amazonaws.dynamodb#StringSetAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.string_attribute_value

StringSetAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.string_attribute_value.StringAttributeValue"
]
