"""Generated from Smithy shape ``com.amazonaws.aiops#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_aiops.types.encryption_configuration_type
    import capo_aiops.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    type: NotRequired[
        "capo_aiops.types.encryption_configuration_type.EncryptionConfigurationType"
    ]
    """<p>Displays whether investigation data is encrypted by a customer managed key or an Amazon Web Services owned key.</p>"""
    kms_key_id: NotRequired["capo_aiops.types.kms_key_id.KmsKeyId"]
    """<p>If the investigation group uses a customer managed key for encryption, this field displays the ID of that key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_aiops.types.encryption_configuration_type

        out["type"] = capo_aiops.types.encryption_configuration_type.serialize_json(
            value["type"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_aiops.types.encryption_configuration_type

        out["type"] = capo_aiops.types.encryption_configuration_type.deserialize_json(
            data["type"]
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
