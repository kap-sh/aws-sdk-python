"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ReferenceDataSourceUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.bucket_arn
    import aws_sdk_kinesis_analytics_v2.types.file_key


class S3ReferenceDataSourceUpdate(TypedDict):
    bucket_arn_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    file_key_update: NotRequired["aws_sdk_kinesis_analytics_v2.types.file_key.FileKey"]
    """<p>The object key name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReferenceDataSourceUpdate) -> dict:
    out: dict = {}
    if "bucket_arn_update" in value:
        out["BucketARNUpdate"] = value["bucket_arn_update"]
    if "file_key_update" in value:
        out["FileKeyUpdate"] = value["file_key_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReferenceDataSourceUpdate:
    out: S3ReferenceDataSourceUpdate = {}  # type: ignore[typeddict-item]
    if "BucketARNUpdate" in data:
        out["bucket_arn_update"] = data["BucketARNUpdate"]
    if "FileKeyUpdate" in data:
        out["file_key_update"] = data["FileKeyUpdate"]
    return out
