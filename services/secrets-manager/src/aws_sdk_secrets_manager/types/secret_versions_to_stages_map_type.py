"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionsToStagesMapType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stages_type

SecretVersionsToStagesMapType: TypeAlias = dict[
    "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType",
    "aws_sdk_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType",
]
