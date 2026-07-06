"""Generated from Smithy shape ``com.amazonaws.proton#S3ObjectSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.s3_bucket
    import aws_sdk_proton.types.s3_key


class S3ObjectSource(TypedDict, closed=True):
    bucket: "aws_sdk_proton.types.s3_bucket.S3Bucket"
    """<p>The name of the S3 bucket that contains a template bundle.</p>"""
    key: "aws_sdk_proton.types.s3_key.S3Key"
    """<p>The path to the S3 bucket that contains a template bundle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ObjectSource) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ObjectSource:
    out: S3ObjectSource = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3ObjectSource.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3ObjectSource.key required")
    return out
