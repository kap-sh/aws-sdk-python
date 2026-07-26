"""Generated from Smithy shape ``com.amazonaws.panorama#StorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.bucket
    import capo_panorama.types.object


class StorageLocation(TypedDict, closed=True):
    bucket: "capo_panorama.types.bucket.Bucket"
    """<p>The location's bucket.</p>"""
    repo_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's repo prefix.</p>"""
    generated_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's generated prefix.</p>"""
    binary_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's binary prefix.</p>"""
    manifest_prefix_location: "capo_panorama.types.object.Object"
    """<p>The location's manifest prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageLocation) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["RepoPrefixLocation"] = value["repo_prefix_location"]
    out["GeneratedPrefixLocation"] = value["generated_prefix_location"]
    out["BinaryPrefixLocation"] = value["binary_prefix_location"]
    out["ManifestPrefixLocation"] = value["manifest_prefix_location"]
    return out


def deserialize_json(data: dict) -> StorageLocation:
    out: StorageLocation = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("StorageLocation.bucket required")
    if "RepoPrefixLocation" in data:
        out["repo_prefix_location"] = data["RepoPrefixLocation"]
    else:
        raise DeserializationError("StorageLocation.repo_prefix_location required")
    if "GeneratedPrefixLocation" in data:
        out["generated_prefix_location"] = data["GeneratedPrefixLocation"]
    else:
        raise DeserializationError("StorageLocation.generated_prefix_location required")
    if "BinaryPrefixLocation" in data:
        out["binary_prefix_location"] = data["BinaryPrefixLocation"]
    else:
        raise DeserializationError("StorageLocation.binary_prefix_location required")
    if "ManifestPrefixLocation" in data:
        out["manifest_prefix_location"] = data["ManifestPrefixLocation"]
    else:
        raise DeserializationError("StorageLocation.manifest_prefix_location required")
    return out
