"""Generated from Smithy shape ``com.amazonaws.ivs#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.s3_destination_bucket_name


class S3DestinationConfiguration(TypedDict):
    bucket_name: "aws_sdk_ivs.types.s3_destination_bucket_name.S3DestinationBucketName"
    """<p>Location (S3 bucket name) where recorded videos will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfiguration) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> S3DestinationConfiguration:
    out: S3DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3DestinationConfiguration.bucket_name required")
    return out
