"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.kms_key_arn
    import capo_inspector2.types.resource_type
    import capo_inspector2.types.scan_type


class UpdateEncryptionKeyRequest(TypedDict, closed=True):
    kms_key_id: "capo_inspector2.types.kms_key_arn.KmsKeyArn"
    """<p>A KMS key ID for the encryption key.</p>"""
    scan_type: "capo_inspector2.types.scan_type.ScanType"
    """<p>The scan type for the encryption key.</p>"""
    resource_type: "capo_inspector2.types.resource_type.ResourceType"
    """<p>The resource type for the encryption key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEncryptionKeyRequest) -> dict:
    out: dict = {}
    out["kmsKeyId"] = value["kms_key_id"]
    out["scanType"] = value["scan_type"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> UpdateEncryptionKeyRequest:
    out: UpdateEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("UpdateEncryptionKeyRequest.kms_key_id required")
    if "scanType" in data:
        out["scan_type"] = data["scanType"]
    else:
        raise DeserializationError("UpdateEncryptionKeyRequest.scan_type required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("UpdateEncryptionKeyRequest.resource_type required")
    return out
