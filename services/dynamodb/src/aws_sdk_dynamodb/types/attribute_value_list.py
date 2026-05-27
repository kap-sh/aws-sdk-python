"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_value

AttributeValueList: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue"
]
