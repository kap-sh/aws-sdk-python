"""Generated from Smithy shape ``com.amazonaws.kms#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.tag_key_type

TagKeyList: TypeAlias = list["aws_sdk_kms.types.tag_key_type.TagKeyType"]
