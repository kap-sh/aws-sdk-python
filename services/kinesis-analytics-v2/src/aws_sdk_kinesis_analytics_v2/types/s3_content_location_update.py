"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ContentLocationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.bucket_arn
    import aws_sdk_kinesis_analytics_v2.types.file_key
    import aws_sdk_kinesis_analytics_v2.types.object_version


class S3ContentLocationUpdate(TypedDict):
    bucket_arn_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    ]
    """<p>The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.</p>"""
    file_key_update: NotRequired["aws_sdk_kinesis_analytics_v2.types.file_key.FileKey"]
    """<p>The new file key for the object containing the application code.</p>"""
    object_version_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.object_version.ObjectVersion"
    ]
    """<p>The new version of the object containing the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ContentLocationUpdate) -> dict:
    out: dict = {}
    if "bucket_arn_update" in value:
        out["BucketARNUpdate"] = value["bucket_arn_update"]
    if "file_key_update" in value:
        out["FileKeyUpdate"] = value["file_key_update"]
    if "object_version_update" in value:
        out["ObjectVersionUpdate"] = value["object_version_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ContentLocationUpdate:
    out: S3ContentLocationUpdate = {}  # type: ignore[typeddict-item]
    if "BucketARNUpdate" in data:
        out["bucket_arn_update"] = data["BucketARNUpdate"]
    if "FileKeyUpdate" in data:
        out["file_key_update"] = data["FileKeyUpdate"]
    if "ObjectVersionUpdate" in data:
        out["object_version_update"] = data["ObjectVersionUpdate"]
    return out
