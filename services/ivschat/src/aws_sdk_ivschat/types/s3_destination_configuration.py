"""Generated from Smithy shape ``com.amazonaws.ivschat#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.bucket_name


class S3DestinationConfiguration(TypedDict):
    bucket_name: "aws_sdk_ivschat.types.bucket_name.BucketName"
    """<p>Name of the Amazon S3 bucket where chat activity will be logged.</p>"""


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
