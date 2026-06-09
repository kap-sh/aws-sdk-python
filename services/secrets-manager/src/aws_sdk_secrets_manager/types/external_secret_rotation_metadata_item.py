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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalSecretRotationMetadataItem) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalSecretRotationMetadataItem:
    out: ExternalSecretRotationMetadataItem = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
