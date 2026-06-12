"""Generated from Smithy shape ``com.amazonaws.customerprofiles#S3ExportingLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.s3_bucket_name
    import aws_sdk_customer_profiles.types.s3_key_name


class S3ExportingLocation(TypedDict):
    s3_bucket_name: NotRequired[
        "aws_sdk_customer_profiles.types.s3_bucket_name.s3BucketName"
    ]
    """<p>The name of the S3 bucket name where Identity Resolution Jobs write result files.</p>"""
    s3_key_name: NotRequired["aws_sdk_customer_profiles.types.s3_key_name.s3KeyName"]
    """<p>The S3 key name of the location where Identity Resolution Jobs write result files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportingLocation) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key_name" in value:
        out["S3KeyName"] = value["s3_key_name"]
    return out


def deserialize_json(data: dict) -> S3ExportingLocation:
    out: S3ExportingLocation = {}  # type: ignore[typeddict-item]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3KeyName" in data:
        out["s3_key_name"] = data["S3KeyName"]
    return out
