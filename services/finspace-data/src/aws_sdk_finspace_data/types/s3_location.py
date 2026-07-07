"""Generated from Smithy shape ``com.amazonaws.finspacedata#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_finspace_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.s3_bucket_name
    import aws_sdk_finspace_data.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket: "aws_sdk_finspace_data.types.s3_bucket_name.S3BucketName"
    """<p> The name of the S3 bucket.</p>"""
    key: "aws_sdk_finspace_data.types.s3_key.S3Key"
    """<p> The path of the folder, within the S3 bucket that contains the Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Location.key required")
    return out
