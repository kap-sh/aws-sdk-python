"""Generated from Smithy shape ``com.amazonaws.kendra#S3Path``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.s3_bucket_name
    import aws_sdk_kendra.types.s3_object_key


class S3Path(TypedDict):
    bucket: "aws_sdk_kendra.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket that contains the file.</p>"""
    key: "aws_sdk_kendra.types.s3_object_key.S3ObjectKey"
    """<p>The name of the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Path) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Path:
    out: S3Path = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    else:
        raise DeserializationError("S3Path.bucket required")
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("S3Path.key required")
    return out
