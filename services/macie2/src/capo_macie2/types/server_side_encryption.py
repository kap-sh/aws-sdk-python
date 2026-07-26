"""Generated from Smithy shape ``com.amazonaws.macie2#ServerSideEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.encryption_type


class ServerSideEncryption(TypedDict, closed=True):
    encryption_type: NotRequired["capo_macie2.types.encryption_type.EncryptionType"]
    """<p>The server-side encryption algorithm that's used when storing data in the bucket or object. If default encryption settings aren't configured for the bucket or the object isn't encrypted using server-side encryption, this value is NONE.</p>"""
    kms_master_key_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) or unique identifier (key ID) for the KMS key that's used to encrypt data in the bucket or the object. This value is null if an KMS key isn't used to encrypt the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryption) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import capo_macie2.types.encryption_type

        out["encryptionType"] = capo_macie2.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    if "kms_master_key_id" in value:
        out["kmsMasterKeyId"] = value["kms_master_key_id"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryption:
    out: ServerSideEncryption = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import capo_macie2.types.encryption_type

        out["encryption_type"] = capo_macie2.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    if "kmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["kmsMasterKeyId"]
    return out
