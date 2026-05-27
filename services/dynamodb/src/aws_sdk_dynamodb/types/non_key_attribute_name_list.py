"""Generated from Smithy shape ``com.amazonaws.dynamodb#NonKeyAttributeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.non_key_attribute_name

NonKeyAttributeNameList: TypeAlias = list[
    "aws_sdk_dynamodb.types.non_key_attribute_name.NonKeyAttributeName"
]
