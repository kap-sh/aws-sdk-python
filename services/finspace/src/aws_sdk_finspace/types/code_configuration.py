"""Generated from Smithy shape ``com.amazonaws.finspace#CodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_finspace.types.s3_bucket
    import aws_sdk_finspace.types.s3_key
    import aws_sdk_finspace.types.s3_object_version


class CodeConfiguration(TypedDict):
    s3_bucket: NotRequired["aws_sdk_finspace.types.s3_bucket.S3Bucket"]
    """<p>A unique name for the S3 bucket.</p>"""
    s3_key: NotRequired["aws_sdk_finspace.types.s3_key.S3Key"]
    """<p>The full S3 path (excluding bucket) to the .zip file. This file contains the code that is loaded onto the cluster when it's started.</p>"""
    s3_object_version: NotRequired[
        "aws_sdk_finspace.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The version of an S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeConfiguration) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["s3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["s3ObjectVersion"] = value["s3_object_version"]
    return out


def deserialize_json(data: dict) -> CodeConfiguration:
    out: CodeConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    if "s3ObjectVersion" in data:
        out["s3_object_version"] = data["s3ObjectVersion"]
    return out
