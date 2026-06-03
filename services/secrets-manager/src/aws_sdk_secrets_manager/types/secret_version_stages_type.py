"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionStagesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_version_stage_type

SecretVersionStagesType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
]
