"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeS3OutputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.account_id
    import aws_sdk_bedrock_runtime.types.kms_key_id
    import aws_sdk_bedrock_runtime.types.s3_uri


class AsyncInvokeS3OutputDataConfig(TypedDict):
    s3_uri: "aws_sdk_bedrock_runtime.types.s3_uri.S3Uri"
    """<p>An object URI starting with <code>s3://</code>.</p>"""
    kms_key_id: NotRequired["aws_sdk_bedrock_runtime.types.kms_key_id.KmsKeyId"]
    """<p>A KMS encryption key ID.</p>"""
    bucket_owner: NotRequired["aws_sdk_bedrock_runtime.types.account_id.AccountId"]
    """<p>If the bucket belongs to another AWS account, specify that account's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeS3OutputDataConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> AsyncInvokeS3OutputDataConfig:
    out: AsyncInvokeS3OutputDataConfig = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    else:
        raise DeserializationError("AsyncInvokeS3OutputDataConfig.s3_uri required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "bucketOwner" in data:
        out["bucket_owner"] = data["bucketOwner"]
    return out
