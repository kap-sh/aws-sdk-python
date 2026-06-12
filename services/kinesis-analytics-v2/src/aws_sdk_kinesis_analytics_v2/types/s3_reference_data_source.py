"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ReferenceDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.bucket_arn
    import aws_sdk_kinesis_analytics_v2.types.file_key


class S3ReferenceDataSource(TypedDict):
    bucket_arn: NotRequired["aws_sdk_kinesis_analytics_v2.types.bucket_arn.BucketARN"]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    file_key: NotRequired["aws_sdk_kinesis_analytics_v2.types.file_key.FileKey"]
    """<p>The object key name containing the reference data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReferenceDataSource) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["BucketARN"] = value["bucket_arn"]
    if "file_key" in value:
        out["FileKey"] = value["file_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReferenceDataSource:
    out: S3ReferenceDataSource = {}  # type: ignore[typeddict-item]
    if "BucketARN" in data:
        out["bucket_arn"] = data["BucketARN"]
    if "FileKey" in data:
        out["file_key"] = data["FileKey"]
    return out
