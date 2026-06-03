"""Generated from Smithy shape ``com.amazonaws.secretsmanager#TagKeyListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.tag_key_type

TagKeyListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.tag_key_type.TagKeyType"
]
