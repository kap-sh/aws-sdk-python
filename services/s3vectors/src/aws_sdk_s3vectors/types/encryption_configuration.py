"""Generated from Smithy shape ``com.amazonaws.s3vectors#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.kms_key_arn
    import aws_sdk_s3vectors.types.sse_type

class EncryptionConfiguration(TypedDict):
    sse_type: "aws_sdk_s3vectors.types.sse_type.SseType"
    """<p>The server-side encryption type to use for the encryption configuration of the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically <code>AES256</code>.</p>"""
    kms_key_arn: NotRequired["aws_sdk_s3vectors.types.kms_key_arn.KmsKeyArn"]
    """<p>Amazon Web Services Key Management Service (KMS) customer managed key ID to use for the encryption configuration. This parameter is allowed if and only if <code>sseType</code> is set to <code>aws:kms</code>.</p> <p>To specify the KMS key, you must use the format of the KMS key Amazon Resource Name (ARN).</p> <p>For example, specify Key ARN in the following format: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_s3vectors.types.sse_type
    out["sseType"] = aws_sdk_s3vectors.types.sse_type.serialize_json(value.get("sse_type", 'AES256'))
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "sseType" in data:
        import aws_sdk_s3vectors.types.sse_type
        out["sse_type"] = aws_sdk_s3vectors.types.sse_type.deserialize_json(data["sseType"])
    else:
        out["sse_type"] = 'AES256'
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out