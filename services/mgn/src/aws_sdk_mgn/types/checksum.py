"""Generated from Smithy shape ``com.amazonaws.mgn#Checksum``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mgn.types.encryption_algorithm
    import aws_sdk_mgn.types.hash

class Checksum(TypedDict):
    encryption_algorithm: NotRequired["aws_sdk_mgn.types.encryption_algorithm.EncryptionAlgorithm"]
    """<p>The encryption algorithm used to generate the checksum.</p>"""
    hash: NotRequired["aws_sdk_mgn.types.hash.Hash"]
    """<p>The hash value of the checksum.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Checksum) -> dict:
    out: dict = {}
    if "encryption_algorithm" in value:
        out["encryptionAlgorithm"] = value["encryption_algorithm"]
    if "hash" in value:
        out["hash"] = value["hash"]
    return out


def deserialize_json(data: dict) -> Checksum:
    out: Checksum = {}  # type: ignore[typeddict-item]
    if "encryptionAlgorithm" in data:
        out["encryption_algorithm"] = data["encryptionAlgorithm"]
    if "hash" in data:
        out["hash"] = data["hash"]
    return out