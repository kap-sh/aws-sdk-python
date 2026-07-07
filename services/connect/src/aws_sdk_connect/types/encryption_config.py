"""Generated from Smithy shape ``com.amazonaws.connect#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.encryption_type
    import aws_sdk_connect.types.key_id


class EncryptionConfig(TypedDict, closed=True):
    encryption_type: "aws_sdk_connect.types.encryption_type.EncryptionType"
    """<p>The type of encryption.</p>"""
    key_id: "aws_sdk_connect.types.key_id.KeyId"
    r"""<p>The full ARN of the encryption key. </p> <note> <p>Be sure to provide the full ARN of the encryption key, not just the ID.</p> <p>Connect Customer supports only KMS keys with the default key spec of <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default\"> <code>SYMMETRIC_DEFAULT</code> </a>. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.encryption_type

    out["EncryptionType"] = aws_sdk_connect.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    out["KeyId"] = value["key_id"]
    return out


def deserialize_json(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if "EncryptionType" in data:
        import aws_sdk_connect.types.encryption_type

        out["encryption_type"] = aws_sdk_connect.types.encryption_type.deserialize_json(
            data["EncryptionType"]
        )
    else:
        raise DeserializationError("EncryptionConfig.encryption_type required")
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("EncryptionConfig.key_id required")
    return out
