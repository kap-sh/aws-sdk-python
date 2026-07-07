"""Generated from Smithy shape ``com.amazonaws.macie2#ServerSideEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.encryption_type


class ServerSideEncryption(TypedDict, closed=True):
    encryption_type: NotRequired["aws_sdk_macie2.types.encryption_type.EncryptionType"]
    """<p>The server-side encryption algorithm that's used when storing data in the bucket or object. If default encryption settings aren't configured for the bucket or the object isn't encrypted using server-side encryption, this value is NONE.</p>"""
    kms_master_key_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key that's used to encrypt data in the bucket or the object. This value is null if an KMS key isn't used to encrypt the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryption) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import aws_sdk_macie2.types.encryption_type

        out["encryptionType"] = aws_sdk_macie2.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    if "kms_master_key_id" in value:
        out["kmsMasterKeyId"] = value["kms_master_key_id"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryption:
    out: ServerSideEncryption = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_macie2.types.encryption_type

        out["encryption_type"] = aws_sdk_macie2.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    if "kmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["kmsMasterKeyId"]
    return out
