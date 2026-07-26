"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ExternalSecretRotationMetadataType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.external_secret_rotation_metadata_item

ExternalSecretRotationMetadataType: TypeAlias = list[
    "capo_secrets_manager.types.external_secret_rotation_metadata_item.ExternalSecretRotationMetadataItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalSecretRotationMetadataType) -> list:
    import capo_secrets_manager.types.external_secret_rotation_metadata_item

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.external_secret_rotation_metadata_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExternalSecretRotationMetadataType:
    import capo_secrets_manager.types.external_secret_rotation_metadata_item

    out: ExternalSecretRotationMetadataType = []
    for item in data:
        out.append(
            capo_secrets_manager.types.external_secret_rotation_metadata_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
