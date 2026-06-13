"""Generated from Smithy shape ``com.amazonaws.mgn#EnrichmentTargetS3Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.s3_bucket_name
    import aws_sdk_mgn.types.s3_key_name


class EnrichmentTargetS3Configuration(TypedDict):
    s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket where the enriched import file will be stored.</p>"""
    s3_bucket_owner: "aws_sdk_mgn.types.account_id.AccountID"
    """<p>The AWS account ID of the target S3 bucket owner.</p>"""
    s3_key: "aws_sdk_mgn.types.s3_key_name.S3KeyName"
    """<p>The S3 key (path) where the enriched import file will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnrichmentTargetS3Configuration) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3BucketOwner"] = value["s3_bucket_owner"]
    out["s3Key"] = value["s3_key"]
    return out


def deserialize_json(data: dict) -> EnrichmentTargetS3Configuration:
    out: EnrichmentTargetS3Configuration = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("EnrichmentTargetS3Configuration.s3_bucket required")
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    else:
        raise DeserializationError(
            "EnrichmentTargetS3Configuration.s3_bucket_owner required"
        )
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    else:
        raise DeserializationError("EnrichmentTargetS3Configuration.s3_key required")
    return out
