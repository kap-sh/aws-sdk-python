"""Generated from Smithy shape ``com.amazonaws.groundstation#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.s3_bucket_name
    import capo_groundstation.types.s3_object_key
    import capo_groundstation.types.s3_version_id


class S3Object(TypedDict, closed=True):
    bucket: NotRequired["capo_groundstation.types.s3_bucket_name.S3BucketName"]
    """<p>An Amazon S3 Bucket name.</p>"""
    key: NotRequired["capo_groundstation.types.s3_object_key.S3ObjectKey"]
    """<p>An Amazon S3 key for the ephemeris.</p>"""
    version: NotRequired["capo_groundstation.types.s3_version_id.S3VersionId"]
    """<p>For versioned Amazon S3 objects, the version to use for the ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    if "key" in data:
        out["key"] = data["key"]
    if "version" in data:
        out["version"] = data["version"]
    return out
