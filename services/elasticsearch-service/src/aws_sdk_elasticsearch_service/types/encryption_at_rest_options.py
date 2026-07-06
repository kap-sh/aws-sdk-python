"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.kms_key_id


class EncryptionAtRestOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_elasticsearch_service.types.boolean.Boolean"]
    """<p>Specifies the option to enable Encryption At Rest.</p>"""
    kms_key_id: NotRequired["aws_sdk_elasticsearch_service.types.kms_key_id.KmsKeyId"]
    """<p> Specifies the KMS Key ID for Encryption At Rest options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptions:
    out: EncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
