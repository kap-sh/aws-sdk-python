"""Generated from Smithy shape ``com.amazonaws.qbusiness#S3``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.s3_bucket_name
    import capo_qbusiness.types.s3_object_key


class S3(TypedDict, closed=True):
    bucket: "capo_qbusiness.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket that contains the file.</p>"""
    key: "capo_qbusiness.types.s3_object_key.S3ObjectKey"
    """<p>The name of the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3:
    out: S3 = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3.bucket required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3.key required")
    return out
