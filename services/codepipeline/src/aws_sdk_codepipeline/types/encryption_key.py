"""Generated from Smithy shape ``com.amazonaws.codepipeline#EncryptionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.encryption_key_id
    import aws_sdk_codepipeline.types.encryption_key_type


class EncryptionKey(TypedDict, closed=True):
    id: "aws_sdk_codepipeline.types.encryption_key_id.EncryptionKeyId"
    """<p>The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.</p> <note> <p>Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).</p> </note>"""
    type: "aws_sdk_codepipeline.types.encryption_key_type.EncryptionKeyType"
    """<p>The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to 'KMS'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKey) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_codepipeline.types.encryption_key_type

    out["type"] = aws_sdk_codepipeline.types.encryption_key_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKey:
    out: EncryptionKey = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EncryptionKey.id required")
    if "type" in data:
        import aws_sdk_codepipeline.types.encryption_key_type

        out["type"] = (
            aws_sdk_codepipeline.types.encryption_key_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        raise DeserializationError("EncryptionKey.type required")
    return out
