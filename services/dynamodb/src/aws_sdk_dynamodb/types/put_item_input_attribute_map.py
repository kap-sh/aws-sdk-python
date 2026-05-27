"""Generated from Smithy shape ``com.amazonaws.dynamodb#PutItemInputAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name
    import aws_sdk_dynamodb.types.attribute_value

PutItemInputAttributeMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue",
]
