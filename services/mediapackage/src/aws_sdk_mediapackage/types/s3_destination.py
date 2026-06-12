"""Generated from Smithy shape ``com.amazonaws.mediapackage#S3Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class S3Destination(TypedDict):
    bucket_name: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The name of an S3 bucket within which harvested content will be exported"""
    manifest_key: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The key in the specified S3 bucket where the harvested top-level manifest will be placed."""
    role_arn: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The IAM role used to write to the specified S3 bucket"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    if "manifest_key" in value:
        out["manifestKey"] = value["manifest_key"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    if "manifestKey" in data:
        out["manifest_key"] = data["manifestKey"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
