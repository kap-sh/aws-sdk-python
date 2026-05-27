"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.tag

TagList: TypeAlias = list["aws_sdk_dynamodb.types.tag.Tag"]
