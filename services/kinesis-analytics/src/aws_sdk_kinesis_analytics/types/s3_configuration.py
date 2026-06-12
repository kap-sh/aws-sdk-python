"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#S3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.bucket_arn
    import aws_sdk_kinesis_analytics.types.file_key
    import aws_sdk_kinesis_analytics.types.role_arn


class S3Configuration(TypedDict):
    role_arn: "aws_sdk_kinesis_analytics.types.role_arn.RoleARN"
    """<p>IAM ARN of the role used to access the data.</p>"""
    bucket_arn: "aws_sdk_kinesis_analytics.types.bucket_arn.BucketARN"
    """<p>ARN of the S3 bucket that contains the data.</p>"""
    file_key: "aws_sdk_kinesis_analytics.types.file_key.FileKey"
    """<p>The name of the object that contains the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Configuration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("S3Configuration.role_arn required")
    if "BucketARN" in data:
        out["bucket_arn"] = data["BucketARN"]
    else:
        raise DeserializationError("S3Configuration.bucket_arn required")
    if "FileKey" in data:
        out["file_key"] = data["FileKey"]
    else:
        raise DeserializationError("S3Configuration.file_key required")
    return out
