"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.account_id
    import aws_sdk_bedrock_runtime.types.s3_uri


class S3Location(TypedDict, closed=True):
    uri: "aws_sdk_bedrock_runtime.types.s3_uri.S3Uri"
    """<p>An object URI starting with <code>s3://</code>.</p>"""
    bucket_owner: NotRequired["aws_sdk_bedrock_runtime.types.account_id.AccountId"]
    """<p>If the bucket belongs to another AWS account, specify that account's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    else:
        raise DeserializationError("S3Location.uri required")
    if "bucketOwner" in data:
        out["bucket_owner"] = data["bucketOwner"]
    return out
