"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#S3ReferenceDataSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.bucket_arn
    import capo_kinesis_analytics.types.file_key
    import capo_kinesis_analytics.types.role_arn


class S3ReferenceDataSourceDescription(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics.types.bucket_arn.BucketARN"
    """<p>Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    file_key: "capo_kinesis_analytics.types.file_key.FileKey"
    """<p>Amazon S3 object key name.</p>"""
    reference_role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>ARN of the IAM role that Amazon Kinesis Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReferenceDataSourceDescription) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    out["ReferenceRoleARN"] = value["reference_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReferenceDataSourceDescription:
    out: S3ReferenceDataSourceDescription = {}  # type: ignore[typeddict-item]
    if "BucketARN" in data:
        out["bucket_arn"] = data["BucketARN"]
    else:
        raise DeserializationError(
            "S3ReferenceDataSourceDescription.bucket_arn required"
        )
    if "FileKey" in data:
        out["file_key"] = data["FileKey"]
    else:
        raise DeserializationError("S3ReferenceDataSourceDescription.file_key required")
    if "ReferenceRoleARN" in data:
        out["reference_role_arn"] = data["ReferenceRoleARN"]
    else:
        raise DeserializationError(
            "S3ReferenceDataSourceDescription.reference_role_arn required"
        )
    return out
