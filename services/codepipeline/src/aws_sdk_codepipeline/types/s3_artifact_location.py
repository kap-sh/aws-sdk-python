"""Generated from Smithy shape ``com.amazonaws.codepipeline#S3ArtifactLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.s3_bucket_name
    import aws_sdk_codepipeline.types.s3_object_key


class S3ArtifactLocation(TypedDict):
    bucket_name: "aws_sdk_codepipeline.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket.</p>"""
    object_key: "aws_sdk_codepipeline.types.s3_object_key.S3ObjectKey"
    """<p>The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ArtifactLocation) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["objectKey"] = value["object_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ArtifactLocation:
    out: S3ArtifactLocation = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3ArtifactLocation.bucket_name required")
    if "objectKey" in data:
        out["object_key"] = data["objectKey"]
    else:
        raise DeserializationError("S3ArtifactLocation.object_key required")
    return out
