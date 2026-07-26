"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionStagesType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_version_stage_type

SecretVersionStagesType: TypeAlias = list[
    "capo_secrets_manager.types.secret_version_stage_type.SecretVersionStageType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretVersionStagesType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecretVersionStagesType:
    return list(data)
