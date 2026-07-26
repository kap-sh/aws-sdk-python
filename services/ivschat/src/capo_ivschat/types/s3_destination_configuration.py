"""Generated from Smithy shape ``com.amazonaws.ivschat#S3DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivschat.types.bucket_name


class S3DestinationConfiguration(TypedDict, closed=True):
    bucket_name: "capo_ivschat.types.bucket_name.BucketName"
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
