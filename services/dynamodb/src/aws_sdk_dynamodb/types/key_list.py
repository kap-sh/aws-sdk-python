"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.key

KeyList: TypeAlias = list["aws_sdk_dynamodb.types.key.Key"]
