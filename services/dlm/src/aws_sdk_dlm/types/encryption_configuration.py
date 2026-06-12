"""Generated from Smithy shape ``com.amazonaws.dlm#EncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cmk_arn
    import aws_sdk_dlm.types.encrypted


class EncryptionConfiguration(TypedDict):
    encrypted: NotRequired["aws_sdk_dlm.types.encrypted.Encrypted"]
    """<p>To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.</p>"""
    cmk_arn: NotRequired["aws_sdk_dlm.types.cmk_arn.CmkArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "cmk_arn" in value:
        out["CmkArn"] = value["cmk_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "CmkArn" in data:
        out["cmk_arn"] = data["CmkArn"]
    return out
