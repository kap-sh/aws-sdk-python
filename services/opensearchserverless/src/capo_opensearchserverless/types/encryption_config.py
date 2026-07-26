"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#EncryptionConfig``."""

from typing_extensions import NotRequired, TypedDict


class EncryptionConfig(TypedDict, closed=True):
    a_ws_owned_key: NotRequired["bool"]
    """<p>Indicates whether to use an Amazon Web Services-owned key for encryption.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The ARN of the Amazon Web Services Key Management Service key used to encrypt the collection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfig) -> dict:
    out: dict = {}
    if "a_ws_owned_key" in value:
        out["aWSOwnedKey"] = value["a_ws_owned_key"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "aWSOwnedKey" in data:
        out["a_ws_owned_key"] = data["aWSOwnedKey"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
