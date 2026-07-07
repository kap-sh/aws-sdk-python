"""Generated from Smithy shape ``com.amazonaws.mgn#StartExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.s3_bucket_name
    import aws_sdk_mgn.types.s3_key
    import aws_sdk_mgn.types.tags_map


class StartExportRequest(TypedDict, closed=True):
    s3_bucket: "aws_sdk_mgn.types.s3_bucket_name.S3BucketName"
    """<p>Start export request s3 bucket.</p>"""
    s3_key: "aws_sdk_mgn.types.s3_key.S3Key"
    """<p>Start export request s3key.</p>"""
    s3_bucket_owner: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Start export request s3 bucket owner.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Start import request tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportRequest) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartExportRequest:
    out: StartExportRequest = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        raise DeserializationError("StartExportRequest.s3_bucket required")
    if "s3Key" in data:
        out["s3_key"] = data["s3Key"]
    else:
        raise DeserializationError("StartExportRequest.s3_key required")
    if "s3BucketOwner" in data:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    return out
