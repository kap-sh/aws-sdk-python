"""Generated from Smithy shape ``com.amazonaws.appflow#SuccessResponseHandlingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.bucket_name
    import aws_sdk_appflow.types.bucket_prefix


class SuccessResponseHandlingConfig(TypedDict):
    bucket_prefix: NotRequired["aws_sdk_appflow.types.bucket_prefix.BucketPrefix"]
    """<p>The Amazon S3 bucket prefix.</p>"""
    bucket_name: NotRequired["aws_sdk_appflow.types.bucket_name.BucketName"]
    """<p>The name of the Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuccessResponseHandlingConfig) -> dict:
    out: dict = {}
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> SuccessResponseHandlingConfig:
    out: SuccessResponseHandlingConfig = {}  # type: ignore[typeddict-item]
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    return out
