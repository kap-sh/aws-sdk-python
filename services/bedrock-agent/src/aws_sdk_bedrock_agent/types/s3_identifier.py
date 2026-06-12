"""Generated from Smithy shape ``com.amazonaws.bedrockagent#S3Identifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.s3_bucket_name
    import aws_sdk_bedrock_agent.types.s3_object_key


class S3Identifier(TypedDict):
    s3_bucket_name: NotRequired[
        "aws_sdk_bedrock_agent.types.s3_bucket_name.S3BucketName"
    ]
    """<p>The name of the S3 bucket.</p>"""
    s3_object_key: NotRequired["aws_sdk_bedrock_agent.types.s3_object_key.S3ObjectKey"]
    """<p>The S3 object key for the S3 resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Identifier) -> dict:
    out: dict = {}
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "s3_object_key" in value:
        out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_json(data: dict) -> S3Identifier:
    out: S3Identifier = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    if "s3ObjectKey" in data:
        out["s3_object_key"] = data["s3ObjectKey"]
    return out
