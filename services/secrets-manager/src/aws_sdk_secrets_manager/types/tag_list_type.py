"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TagListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.tag

TagListType: TypeAlias = list["aws_sdk_secrets_manager.types.tag.Tag"]
