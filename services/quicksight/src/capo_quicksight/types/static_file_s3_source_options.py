"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFileS3SourceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class StaticFileS3SourceOptions(TypedDict, closed=True):
    bucket_name: "capo_quicksight.types.string.String"
    """<p>The name of the Amazon S3 bucket.</p>"""
    object_key: "capo_quicksight.types.string.String"
    """<p>The identifier of the static file in the Amazon S3 bucket.</p>"""
    region: "capo_quicksight.types.string.String"
    """<p>The Region of the Amazon S3 account that contains the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticFileS3SourceOptions) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> StaticFileS3SourceOptions:
    out: StaticFileS3SourceOptions = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("StaticFileS3SourceOptions.bucket_name required")
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    else:
        raise DeserializationError("StaticFileS3SourceOptions.object_key required")
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("StaticFileS3SourceOptions.region required")
    return out
