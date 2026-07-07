"""Generated from Smithy shape ``com.amazonaws.inspector2#ResetEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.resource_type
    import aws_sdk_inspector2.types.scan_type


class ResetEncryptionKeyRequest(TypedDict, closed=True):
    scan_type: "aws_sdk_inspector2.types.scan_type.ScanType"
    """<p>The scan type the key encrypts.</p>"""
    resource_type: "aws_sdk_inspector2.types.resource_type.ResourceType"
    """<p>The resource type the key encrypts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEncryptionKeyRequest) -> dict:
    out: dict = {}
    out["scanType"] = value["scan_type"]
    out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResetEncryptionKeyRequest:
    out: ResetEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    if "scanType" in data:
        out["scan_type"] = data["scanType"]
    else:
        raise DeserializationError("ResetEncryptionKeyRequest.scan_type required")
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ResetEncryptionKeyRequest.resource_type required")
    return out
