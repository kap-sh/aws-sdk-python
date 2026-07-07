"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#S3DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.s3_bucket_name
    import aws_sdk_mediapackagev2.types.s3_destination_path


class S3DestinationConfig(TypedDict, closed=True):
    bucket_name: "aws_sdk_mediapackagev2.types.s3_bucket_name.S3BucketName"
    """<p>The name of an S3 bucket within which harvested content will be exported.</p>"""
    destination_path: (
        "aws_sdk_mediapackagev2.types.s3_destination_path.S3DestinationPath"
    )
    """<p>The path within the specified S3 bucket where the harvested content will be placed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfig) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["DestinationPath"] = value["destination_path"]
    return out


def deserialize_json(data: dict) -> S3DestinationConfig:
    out: S3DestinationConfig = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3DestinationConfig.bucket_name required")
    if "DestinationPath" in data:
        out["destination_path"] = data["DestinationPath"]
    else:
        raise DeserializationError("S3DestinationConfig.destination_path required")
    return out
