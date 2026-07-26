"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.s3_bucket
    import capo_migrationhubstrategy.types.s3_key


class S3Object(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_migrationhubstrategy.types.s3_bucket.S3Bucket"]
    """<p> The S3 bucket name. </p>"""
    s3key: NotRequired["capo_migrationhubstrategy.types.s3_key.S3Key"]
    """<p> The Amazon S3 key name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3key" in value:
        out["s3key"] = value["s3key"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3key" in data:
        out["s3key"] = data["s3key"]
    return out
