"""Generated from Smithy shape ``com.amazonaws.dynamodb#MapAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name
    import aws_sdk_dynamodb.types.attribute_value

MapAttributeValue: TypeAlias = dict[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue",
]
