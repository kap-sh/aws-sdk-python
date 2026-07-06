"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#S3ReportOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.aws_account_id
    import aws_sdk_resiliencehubv2.types.s3_bucket_path


class S3ReportOutputConfiguration(TypedDict, closed=True):
    bucket_path: "aws_sdk_resiliencehubv2.types.s3_bucket_path.S3BucketPath"
    """<p>S3 bucket path where reports will be written (e.g., my-bucket/ngrh-reports/).</p>"""
    bucket_owner: "aws_sdk_resiliencehubv2.types.aws_account_id.AwsAccountId"
    """<p>Account ID of the bucket owner for cross-account access verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ReportOutputConfiguration) -> dict:
    out: dict = {}
    out["bucketPath"] = value["bucket_path"]
    out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3ReportOutputConfiguration:
    out: S3ReportOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketPath" in data:
        out["bucket_path"] = data["bucketPath"]
    else:
        raise DeserializationError("S3ReportOutputConfiguration.bucket_path required")
    if "bucketOwner" in data:
        out["bucket_owner"] = data["bucketOwner"]
    else:
        raise DeserializationError("S3ReportOutputConfiguration.bucket_owner required")
    return out
