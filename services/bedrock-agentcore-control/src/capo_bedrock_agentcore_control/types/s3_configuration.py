"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.aws_account_id
    import capo_bedrock_agentcore_control.types.s3_bucket_uri


class S3Configuration(TypedDict, closed=True):
    uri: NotRequired["capo_bedrock_agentcore_control.types.s3_bucket_uri.S3BucketUri"]
    """<p>The URI of the Amazon S3 object. This URI specifies the location of the object in Amazon S3.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_bedrock_agentcore_control.types.aws_account_id.AwsAccountId"
    ]
    """<p>The account ID of the Amazon S3 bucket owner. This ID is used for cross-account access to the bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Configuration) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    return out


def deserialize_json(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    return out
