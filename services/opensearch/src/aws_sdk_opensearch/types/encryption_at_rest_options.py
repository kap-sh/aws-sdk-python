"""Generated from Smithy shape ``com.amazonaws.opensearch#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.kms_key_id


class EncryptionAtRestOptions(TypedDict):
    enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>True to enable encryption at rest.</p>"""
    kms_key_id: NotRequired["aws_sdk_opensearch.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key ID. Takes the form <code>1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a</code>.</p>"""


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
