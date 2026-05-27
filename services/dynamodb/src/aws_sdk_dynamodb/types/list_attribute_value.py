"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_value

ListAttributeValue: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue"
]
