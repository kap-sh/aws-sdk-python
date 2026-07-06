"""Generated from Smithy shape ``com.amazonaws.deadline#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.s3_bucket_name
    import aws_sdk_deadline.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket_name: "aws_sdk_deadline.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket.</p>"""
    key: "aws_sdk_deadline.types.s3_key.S3Key"
    """<p>The Amazon S3 object key that uniquely identifies the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Location.bucket_name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Location.key required")
    return out
