"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExpressionAttributeNameMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_name_variable
    import aws_sdk_dynamodb.types.attribute_name

ExpressionAttributeNameMap: TypeAlias = dict[
    "aws_sdk_dynamodb.types.expression_attribute_name_variable.ExpressionAttributeNameVariable",
    "aws_sdk_dynamodb.types.attribute_name.AttributeName",
]
