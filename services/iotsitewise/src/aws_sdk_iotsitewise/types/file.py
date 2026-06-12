"""Generated from Smithy shape ``com.amazonaws.iotsitewise#File``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.bucket
    import aws_sdk_iotsitewise.types.string


class File(TypedDict):
    bucket: "aws_sdk_iotsitewise.types.bucket.Bucket"
    """<p>The name of the Amazon S3 bucket from which data is imported.</p>"""
    key: "aws_sdk_iotsitewise.types.string.String"
    """<p>The key of the Amazon S3 object that contains your data. Each object has a key that is a unique identifier. Each object has exactly one key.</p>"""
    version_id: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The version ID to identify a specific version of the Amazon S3 object that contains your data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: File) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> File:
    out: File = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("File.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("File.key required")
    if "versionId" in data:
        out["version_id"] = data["versionId"]
    return out
