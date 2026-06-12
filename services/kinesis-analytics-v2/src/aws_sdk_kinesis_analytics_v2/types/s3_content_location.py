"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ContentLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.bucket_arn
    import aws_sdk_kinesis_analytics_v2.types.file_key
    import aws_sdk_kinesis_analytics_v2.types.object_version


class S3ContentLocation(TypedDict):
    bucket_arn: "aws_sdk_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) for the S3 bucket containing the application code.</p>"""
    file_key: "aws_sdk_kinesis_analytics_v2.types.file_key.FileKey"
    """<p>The file key for the object containing the application code.</p>"""
    object_version: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.object_version.ObjectVersion"
    ]
    """<p>The version of the object containing the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ContentLocation) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    if "object_version" in value:
        out["ObjectVersion"] = value["object_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ContentLocation:
    out: S3ContentLocation = {}  # type: ignore[typeddict-item]
    if "BucketARN" in data:
        out["bucket_arn"] = data["BucketARN"]
    else:
        raise DeserializationError("S3ContentLocation.bucket_arn required")
    if "FileKey" in data:
        out["file_key"] = data["FileKey"]
    else:
        raise DeserializationError("S3ContentLocation.file_key required")
    if "ObjectVersion" in data:
        out["object_version"] = data["ObjectVersion"]
    return out
