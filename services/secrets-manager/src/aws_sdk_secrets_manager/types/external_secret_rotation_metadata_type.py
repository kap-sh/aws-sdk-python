"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ExternalSecretRotationMetadataType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item

ExternalSecretRotationMetadataType: TypeAlias = list[
    "aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item.ExternalSecretRotationMetadataItem"
]
