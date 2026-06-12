"""Generated from Smithy shape ``com.amazonaws.imagebuilder#S3Logs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string


class S3Logs(TypedDict):
    s3_bucket_name: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The S3 bucket in which to store the logs.</p>"""
    s3_key_prefix: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon S3 path to the bucket where the logs are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Logs) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_json(data: dict) -> S3Logs:
    out: S3Logs = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    if "s3KeyPrefix" in data:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    return out
