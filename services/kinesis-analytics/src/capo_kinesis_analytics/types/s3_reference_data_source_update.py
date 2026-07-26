"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#S3ReferenceDataSourceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.bucket_arn
    import capo_kinesis_analytics.types.file_key
    import capo_kinesis_analytics.types.role_arn


class S3ReferenceDataSourceUpdate(TypedDict, closed=True):
    bucket_arn_update: NotRequired["capo_kinesis_analytics.types.bucket_arn.BucketARN"]
    """<p>Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    file_key_update: NotRequired["capo_kinesis_analytics.types.file_key.FileKey"]
    """<p>Object key name.</p>"""
    reference_role_arn_update: NotRequired[
        "capo_kinesis_analytics.types.role_arn.RoleARN"
    ]
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object and populate the in-application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReferenceDataSourceUpdate) -> dict:
    out: dict = {}
    if "bucket_arn_update" in value:
        out["BucketARNUpdate"] = value["bucket_arn_update"]
    if "file_key_update" in value:
        out["FileKeyUpdate"] = value["file_key_update"]
    if "reference_role_arn_update" in value:
        out["ReferenceRoleARNUpdate"] = value["reference_role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReferenceDataSourceUpdate:
    out: S3ReferenceDataSourceUpdate = {}  # type: ignore[typeddict-item]
    if "BucketARNUpdate" in data:
        out["bucket_arn_update"] = data["BucketARNUpdate"]
    if "FileKeyUpdate" in data:
        out["file_key_update"] = data["FileKeyUpdate"]
    if "ReferenceRoleARNUpdate" in data:
        out["reference_role_arn_update"] = data["ReferenceRoleARNUpdate"]
    return out
