"""Generated from Smithy shape ``com.amazonaws.guardduty#DefaultServerSideEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class DefaultServerSideEncryption(TypedDict):
    encryption_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The type of encryption used for objects within the S3 bucket.</p>"""
    kms_master_key_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS encryption key. Only available if the bucket <code>EncryptionType</code> is <code>aws:kms</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultServerSideEncryption) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        out["encryptionType"] = value["encryption_type"]
    if "kms_master_key_arn" in value:
        out["kmsMasterKeyArn"] = value["kms_master_key_arn"]
    return out


def deserialize_json(data: dict) -> DefaultServerSideEncryption:
    out: DefaultServerSideEncryption = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        out["encryption_type"] = data["encryptionType"]
    if "kmsMasterKeyArn" in data:
        out["kms_master_key_arn"] = data["kmsMasterKeyArn"]
    return out
