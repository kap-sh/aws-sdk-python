"""Generated from Smithy shape ``com.amazonaws.dynamodb#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.tag_key_string

TagKeyList: TypeAlias = list["aws_sdk_dynamodb.types.tag_key_string.TagKeyString"]
