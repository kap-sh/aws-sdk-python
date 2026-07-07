"""Generated from Smithy shape ``com.amazonaws.bedrock#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.bucket_name
    import aws_sdk_bedrock.types.key_prefix


class S3Config(TypedDict, closed=True):
    bucket_name: "aws_sdk_bedrock.types.bucket_name.BucketName"
    """<p>S3 bucket name.</p>"""
    key_prefix: NotRequired["aws_sdk_bedrock.types.key_prefix.KeyPrefix"]
    """<p>S3 prefix. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Config) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_json(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("S3Config.bucket_name required")
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    return out
