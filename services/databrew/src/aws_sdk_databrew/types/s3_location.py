"""Generated from Smithy shape ``com.amazonaws.databrew#S3Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.bucket
    import aws_sdk_databrew.types.bucket_owner
    import aws_sdk_databrew.types.key


class S3Location(TypedDict):
    bucket: "aws_sdk_databrew.types.bucket.Bucket"
    """<p>The Amazon S3 bucket name.</p>"""
    key: NotRequired["aws_sdk_databrew.types.key.Key"]
    """<p>The unique name of the object in the bucket.</p>"""
    bucket_owner: NotRequired["aws_sdk_databrew.types.bucket_owner.BucketOwner"]
    """<p>The Amazon Web Services account ID of the bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    if "bucket_owner" in value:
        out["BucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("S3Location.bucket required")
    if "Key" in data:
        out["key"] = data["Key"]
    if "BucketOwner" in data:
        out["bucket_owner"] = data["BucketOwner"]
    return out
