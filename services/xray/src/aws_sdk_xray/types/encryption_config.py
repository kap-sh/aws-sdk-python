"""Generated from Smithy shape ``com.amazonaws.xray#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_xray.types.encryption_status
    import aws_sdk_xray.types.encryption_type
    import aws_sdk_xray.types.string


class EncryptionConfig(TypedDict, closed=True):
    key_id: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>The ID of the KMS key used for encryption, if applicable.</p>"""
    status: NotRequired["aws_sdk_xray.types.encryption_status.EncryptionStatus"]
    """<p>The encryption status. While the status is <code>UPDATING</code>, X-Ray may encrypt data with a combination of the new and old settings.</p>"""
    type: NotRequired["aws_sdk_xray.types.encryption_type.EncryptionType"]
    """<p>The type of encryption. Set to <code>KMS</code> for encryption with KMS keys. Set to <code>NONE</code> for default encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfig) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "status" in value:
        import aws_sdk_xray.types.encryption_status

        out["Status"] = aws_sdk_xray.types.encryption_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        import aws_sdk_xray.types.encryption_type

        out["Type"] = aws_sdk_xray.types.encryption_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    if "Status" in data:
        import aws_sdk_xray.types.encryption_status

        out["status"] = aws_sdk_xray.types.encryption_status.deserialize_json(
            data["Status"]
        )
    if "Type" in data:
        import aws_sdk_xray.types.encryption_type

        out["type"] = aws_sdk_xray.types.encryption_type.deserialize_json(data["Type"])
    return out
