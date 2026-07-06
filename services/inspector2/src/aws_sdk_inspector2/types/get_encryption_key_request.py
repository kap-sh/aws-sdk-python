"""Generated from Smithy shape ``com.amazonaws.inspector2#GetEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.resource_type
    import aws_sdk_inspector2.types.scan_type


class GetEncryptionKeyRequest(TypedDict, closed=True):
    scan_type: "aws_sdk_inspector2.types.scan_type.ScanType"
    """<p>The scan type the key encrypts.</p>"""
    resource_type: "aws_sdk_inspector2.types.resource_type.ResourceType"
    """<p>The resource type the key encrypts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEncryptionKeyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEncryptionKeyRequest:
    out: GetEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    return out
