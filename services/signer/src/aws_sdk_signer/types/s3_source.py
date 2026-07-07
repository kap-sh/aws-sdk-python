"""Generated from Smithy shape ``com.amazonaws.signer#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.bucket_name
    import aws_sdk_signer.types.key
    import aws_sdk_signer.types.version


class S3Source(TypedDict, closed=True):
    bucket_name: "aws_sdk_signer.types.bucket_name.BucketName"
    """<p>Name of the S3 bucket.</p>"""
    key: "aws_sdk_signer.types.key.Key"
    """<p>Key name of the bucket object that contains your unsigned code.</p>"""
    version: "aws_sdk_signer.types.version.Version"
    """<p>Version of your source image in your version enabled S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Source.bucket_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Source.key required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("S3Source.version required")
    return out
