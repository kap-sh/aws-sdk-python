"""Generated from Smithy shape ``com.amazonaws.translate#EncryptionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_translate.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_translate.types.encryption_key_id
    import aws_sdk_translate.types.encryption_key_type


class EncryptionKey(TypedDict, closed=True):
    type: "aws_sdk_translate.types.encryption_key_type.EncryptionKeyType"
    """<p>The type of encryption key used by Amazon Translate to encrypt this object.</p>"""
    id: "aws_sdk_translate.types.encryption_key_id.EncryptionKeyID"
    """<p>The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKey) -> dict:
    out: dict = {}
    import aws_sdk_translate.types.encryption_key_type

    out["Type"] = aws_sdk_translate.types.encryption_key_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKey:
    out: EncryptionKey = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_translate.types.encryption_key_type

        out["type"] = (
            aws_sdk_translate.types.encryption_key_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EncryptionKey.type required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("EncryptionKey.id required")
    return out
