"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.attribute_name

AttributeNameList: TypeAlias = list[
    "aws_sdk_dynamodb.types.attribute_name.AttributeName"
]
