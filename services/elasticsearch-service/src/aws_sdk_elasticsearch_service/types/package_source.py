"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.s3_bucket_name
    import aws_sdk_elasticsearch_service.types.s3_key


class PackageSource(TypedDict):
    s3_bucket_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.s3_bucket_name.S3BucketName"
    ]
    """<p>Name of the bucket containing the package.</p>"""
    s3_key: NotRequired["aws_sdk_elasticsearch_service.types.s3_key.S3Key"]
    """<p>Key (file name) of the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageSource) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["S3BucketName"] = value["s3_bucket_name"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_json(data: dict) -> PackageSource:
    out: PackageSource = {}  # type: ignore[typeddict-item]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    return out
