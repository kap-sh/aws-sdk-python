"""Generated from Smithy shape ``com.amazonaws.cloudtrail#S3ImportSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string


class S3ImportSource(TypedDict):
    s3_location_uri: "aws_sdk_cloudtrail.types.string.String"
    """<p> The URI for the source S3 bucket. </p>"""
    s3_bucket_region: "aws_sdk_cloudtrail.types.string.String"
    """<p> The Region associated with the source S3 bucket. </p>"""
    s3_bucket_access_role_arn: "aws_sdk_cloudtrail.types.string.String"
    """<p> The IAM ARN role used to access the source S3 bucket. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ImportSource) -> dict:
    out: dict = {}
    out["S3LocationUri"] = value["s3_location_uri"]
    out["S3BucketRegion"] = value["s3_bucket_region"]
    out["S3BucketAccessRoleArn"] = value["s3_bucket_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ImportSource:
    out: S3ImportSource = {}  # type: ignore[typeddict-item]
    if "S3LocationUri" in data:
        out["s3_location_uri"] = data["S3LocationUri"]
    else:
        raise DeserializationError("S3ImportSource.s3_location_uri required")
    if "S3BucketRegion" in data:
        out["s3_bucket_region"] = data["S3BucketRegion"]
    else:
        raise DeserializationError("S3ImportSource.s3_bucket_region required")
    if "S3BucketAccessRoleArn" in data:
        out["s3_bucket_access_role_arn"] = data["S3BucketAccessRoleArn"]
    else:
        raise DeserializationError("S3ImportSource.s3_bucket_access_role_arn required")
    return out
