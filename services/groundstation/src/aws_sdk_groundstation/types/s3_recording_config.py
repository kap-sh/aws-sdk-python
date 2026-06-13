"""Generated from Smithy shape ``com.amazonaws.groundstation#S3RecordingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.bucket_arn
    import aws_sdk_groundstation.types.role_arn
    import aws_sdk_groundstation.types.s3_key_prefix


class S3RecordingConfig(TypedDict):
    bucket_arn: "aws_sdk_groundstation.types.bucket_arn.BucketArn"
    """<p>ARN of the bucket to record to.</p>"""
    role_arn: "aws_sdk_groundstation.types.role_arn.RoleArn"
    """<p>ARN of the role Ground Station assumes to write data to the bucket.</p>"""
    prefix: NotRequired["aws_sdk_groundstation.types.s3_key_prefix.S3KeyPrefix"]
    """<p>S3 Key prefix to prefice data files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RecordingConfig) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    out["roleArn"] = value["role_arn"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3RecordingConfig:
    out: S3RecordingConfig = {}  # type: ignore[typeddict-item]
    if "bucketArn" in data:
        out["bucket_arn"] = data["bucketArn"]
    else:
        raise DeserializationError("S3RecordingConfig.bucket_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("S3RecordingConfig.role_arn required")
    if "prefix" in data:
        out["prefix"] = data["prefix"]
    return out
