"""Generated from Smithy shape ``com.amazonaws.quicksight#ManifestFileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.s3_bucket
    import capo_quicksight.types.s3_key


class ManifestFileLocation(TypedDict, closed=True):
    bucket: "capo_quicksight.types.s3_bucket.S3Bucket"
    """<p>Amazon S3 bucket.</p>"""
    key: "capo_quicksight.types.s3_key.S3Key"
    """<p>Amazon S3 key that identifies an object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManifestFileLocation) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_json(data: dict) -> ManifestFileLocation:
    out: ManifestFileLocation = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("ManifestFileLocation.bucket required")
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ManifestFileLocation.key required")
    return out
