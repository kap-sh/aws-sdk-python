"""Generated from Smithy shape ``com.amazonaws.mgn#TargetS3ConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.s3_bucket_name


class TargetS3ConfigurationUpdate(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_mgn.types.s3_bucket_name.S3BucketName"]
    """<p>The updated name of the S3 bucket.</p>"""
    s3_bucket_owner: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The updated AWS account ID of the S3 bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetS3ConfigurationUpdate) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> TargetS3ConfigurationUpdate:
    out: TargetS3ConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    return out
