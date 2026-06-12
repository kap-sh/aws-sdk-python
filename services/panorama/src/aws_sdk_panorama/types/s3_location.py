"""Generated from Smithy shape ``com.amazonaws.panorama#S3Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.bucket_name
    import aws_sdk_panorama.types.object_key
    import aws_sdk_panorama.types.region


class S3Location(TypedDict):
    region: NotRequired["aws_sdk_panorama.types.region.Region"]
    """<p>The bucket's Region.</p>"""
    bucket_name: "aws_sdk_panorama.types.bucket_name.BucketName"
    """<p>A bucket name.</p>"""
    object_key: "aws_sdk_panorama.types.object_key.ObjectKey"
    """<p>An object key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Location.bucket_name required")
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    else:
        raise DeserializationError("S3Location.object_key required")
    return out
