"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ExternalSecretRotationMetadataItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item_key_type
    import aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item_value_type


class ExternalSecretRotationMetadataItem(TypedDict):
    key: NotRequired[
        "aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item_key_type.ExternalSecretRotationMetadataItemKeyType"
    ]
    """<p>The key that identifies the item.</p>"""
    value: NotRequired[
        "aws_sdk_secrets_manager.types.external_secret_rotation_metadata_item_value_type.ExternalSecretRotationMetadataItemValueType"
    ]
    """<p>The value of the specified item.</p>"""
