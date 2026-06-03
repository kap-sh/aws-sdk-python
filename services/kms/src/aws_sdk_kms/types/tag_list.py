"""Generated from Smithy shape ``com.amazonaws.kms#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.tag

TagList: TypeAlias = list["aws_sdk_kms.types.tag.Tag"]
