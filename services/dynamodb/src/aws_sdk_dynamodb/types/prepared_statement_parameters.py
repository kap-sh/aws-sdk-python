"""Generated from Smithy shape ``com.amazonaws.dynamodb#PreparedStatementParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_value

PreparedStatementParameters: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_value.AttributeValue"
]
