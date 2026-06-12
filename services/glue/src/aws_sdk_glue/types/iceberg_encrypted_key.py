"""Generated from Smithy shape ``com.amazonaws.glue#IcebergEncryptedKey``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.encrypted_key_metadata_string
    import aws_sdk_glue.types.encryption_key_id_string
    import aws_sdk_glue.types.string_to_string_map


class IcebergEncryptedKey(TypedDict):
    key_id: "aws_sdk_glue.types.encryption_key_id_string.EncryptionKeyIdString"
    """<p>Unique identifier of the encryption key used for Iceberg table encryption. This ID is used to reference the key in table metadata and track which key was used to encrypt specific data.</p>"""
    encrypted_key_metadata: (
        "aws_sdk_glue.types.encrypted_key_metadata_string.EncryptedKeyMetadataString"
    )
    """<p>Encrypted key and metadata, base64 encoded. The format of encrypted key metadata is determined by the table's encryption scheme and can be a wrapped format specific to the table's KMS provider.</p>"""
    encrypted_by_id: NotRequired[
        "aws_sdk_glue.types.encryption_key_id_string.EncryptionKeyIdString"
    ]
    """<p>Optional ID of the key used to encrypt or wrap the key metadata in Iceberg table encryption. This field references another encryption key that was used to encrypt the current key's metadata.</p>"""
    properties: NotRequired["aws_sdk_glue.types.string_to_string_map.StringToStringMap"]
    """<p>A string to string map of additional metadata used by the table's encryption scheme. These properties provide additional context and configuration for the encryption key implementation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergEncryptedKey) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    out["EncryptedKeyMetadata"] = value["encrypted_key_metadata"]
    if "encrypted_by_id" in value:
        out["EncryptedById"] = value["encrypted_by_id"]
    if "properties" in value:
        import aws_sdk_glue.types.string_to_string_map

        out["Properties"] = (
            aws_sdk_glue.types.string_to_string_map.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergEncryptedKey:
    out: IcebergEncryptedKey = {}  # type: ignore[typeddict-item]
    if "KeyId" in data:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError("IcebergEncryptedKey.key_id required")
    if "EncryptedKeyMetadata" in data:
        out["encrypted_key_metadata"] = data["EncryptedKeyMetadata"]
    else:
        raise DeserializationError(
            "IcebergEncryptedKey.encrypted_key_metadata required"
        )
    if "EncryptedById" in data:
        out["encrypted_by_id"] = data["EncryptedById"]
    if "Properties" in data:
        import aws_sdk_glue.types.string_to_string_map

        out["properties"] = (
            aws_sdk_glue.types.string_to_string_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
