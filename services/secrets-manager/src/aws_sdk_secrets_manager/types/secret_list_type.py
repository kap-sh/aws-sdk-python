"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_list_entry

SecretListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_list_entry.SecretListEntry"
]
