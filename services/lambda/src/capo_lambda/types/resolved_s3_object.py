"""Generated from Smithy shape ``com.amazonaws.lambda#ResolvedS3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.s3_bucket
    import capo_lambda.types.s3_key
    import capo_lambda.types.s3_object_version


class ResolvedS3Object(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_lambda.types.s3_bucket.S3Bucket"]
    """<p>The Amazon S3 bucket that contains the deployment package.</p>"""
    s3_key: NotRequired["capo_lambda.types.s3_key.S3Key"]
    """<p>The Amazon S3 key of the deployment package.</p>"""
    s3_object_version: NotRequired[
        "capo_lambda.types.s3_object_version.S3ObjectVersion"
    ]
    """<p>The version of the deployment package object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolvedS3Object) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_object_version" in value:
        out["S3ObjectVersion"] = value["s3_object_version"]
    return out


def deserialize_json(data: dict) -> ResolvedS3Object:
    out: ResolvedS3Object = {}  # type: ignore[typeddict-item]
    if "S3Bucket" in data:
        out["s3_bucket"] = data["S3Bucket"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    if "S3ObjectVersion" in data:
        out["s3_object_version"] = data["S3ObjectVersion"]
    return out
