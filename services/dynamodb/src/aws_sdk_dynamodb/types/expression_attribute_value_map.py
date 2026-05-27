"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpressionAttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_value_variable
    import aws_sdk_dynamodb.types.attribute_value

ExpressionAttributeValueMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.expression_attribute_value_variable.ExpressionAttributeValueVariable",
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue",
]
