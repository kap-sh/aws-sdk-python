"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretValuesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_value_entry

SecretValuesType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_value_entry.SecretValueEntry"
]
