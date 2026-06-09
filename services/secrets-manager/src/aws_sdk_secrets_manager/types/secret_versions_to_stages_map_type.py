"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretVersionsToStagesMapType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.secret_version_id_type
    import aws_sdk_secrets_manager.types.secret_version_stages_type

SecretVersionsToStagesMapType: TypeAlias = dict[
    "aws_sdk_secrets_manager.types.secret_version_id_type.SecretVersionIdType",
    "aws_sdk_secrets_manager.types.secret_version_stages_type.SecretVersionStagesType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: SecretVersionsToStagesMapType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out[key] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SecretVersionsToStagesMapType:
    out: SecretVersionsToStagesMapType = {}
    for key, value in data.items():
        import aws_sdk_secrets_manager.types.secret_version_stages_type

        out[key] = (
            aws_sdk_secrets_manager.types.secret_version_stages_type.deserialize_aws_json_1_1(
                value
            )
        )
    return out
