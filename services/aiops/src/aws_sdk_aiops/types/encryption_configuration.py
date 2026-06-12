"""Generated from Smithy shape ``com.amazonaws.aiops#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_aiops.types.encryption_configuration_type
    import aws_sdk_aiops.types.kms_key_id


class EncryptionConfiguration(TypedDict):
    type: NotRequired[
        "aws_sdk_aiops.types.encryption_configuration_type.EncryptionConfigurationType"
    ]
    """<p>Displays whether investigation data is encrypted by a customer managed key or an Amazon Web Services owned key.</p>"""
    kms_key_id: NotRequired["aws_sdk_aiops.types.kms_key_id.KmsKeyId"]
    """<p>If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_aiops.types.encryption_configuration_type

        out["type"] = aws_sdk_aiops.types.encryption_configuration_type.serialize_json(
            value["type"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_aiops.types.encryption_configuration_type

        out["type"] = (
            aws_sdk_aiops.types.encryption_configuration_type.deserialize_json(
                data["type"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
