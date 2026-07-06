"""Generated from Smithy shape ``com.amazonaws.panorama#OutPutS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.bucket_name
    import aws_sdk_panorama.types.object_key


class OutPutS3Location(TypedDict, closed=True):
    bucket_name: "aws_sdk_panorama.types.bucket_name.BucketName"
    """<p>The object's bucket.</p>"""
    object_key: "aws_sdk_panorama.types.object_key.ObjectKey"
    """<p>The object's key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutPutS3Location) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> OutPutS3Location:
    out: OutPutS3Location = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("OutPutS3Location.bucket_name required")
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    else:
        raise DeserializationError("OutPutS3Location.object_key required")
    return out
