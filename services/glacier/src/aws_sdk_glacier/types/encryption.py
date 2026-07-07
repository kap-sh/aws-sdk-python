"""Generated from Smithy shape ``com.amazonaws.glacier#Encryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.encryption_type
    import aws_sdk_glacier.types.string


class Encryption(TypedDict, closed=True):
    encryption_type: NotRequired["aws_sdk_glacier.types.encryption_type.EncryptionType"]
    """<p>The server-side encryption algorithm used when storing job results in Amazon S3, for example <code>AES256</code> or <code>aws:kms</code>.</p>"""
    kms_key_id: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The AWS KMS key ID to use for object encryption. All GET and PUT requests for an object protected by AWS KMS fail if not made by using Secure Sockets Layer (SSL) or Signature Version 4. </p>"""
    kms_context: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Optional. If the encryption type is <code>aws:kms</code>, you can use this value to specify the encryption context for the job results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Encryption) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import aws_sdk_glacier.types.encryption_type

        out["EncryptionType"] = aws_sdk_glacier.types.encryption_type.serialize_json(
            value["encryption_type"]
        )
    if "kms_key_id" in value:
        out["KMSKeyId"] = value["kms_key_id"]
    if "kms_context" in value:
        out["KMSContext"] = value["kms_context"]
    return out


def deserialize_json(data: dict) -> Encryption:
    out: Encryption = {}  # type: ignore[typeddict-item]
    if "EncryptionType" in data:
        import aws_sdk_glacier.types.encryption_type

        out["encryption_type"] = aws_sdk_glacier.types.encryption_type.deserialize_json(
            data["EncryptionType"]
        )
    if "KMSKeyId" in data:
        out["kms_key_id"] = data["KMSKeyId"]
    if "KMSContext" in data:
        out["kms_context"] = data["KMSContext"]
    return out
