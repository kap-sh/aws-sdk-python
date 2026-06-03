"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_versions_list_entry

SecretVersionsListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_versions_list_entry.SecretVersionsListEntry"
]
