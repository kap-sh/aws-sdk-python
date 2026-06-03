"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretIdListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_id_type

SecretIdListType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_id_type.SecretIdType"
]
