"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration


class SrtEncryptionConfiguration(TypedDict):
    encryption_key: "aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"
    """<p>Specifies the encryption key configuration used for encrypting SRT streams, including the key source and associated credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtEncryptionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

    out["encryptionKey"] = (
        aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
            value["encryption_key"]
        )
    )
    return out


def deserialize_json(data: dict) -> SrtEncryptionConfiguration:
    out: SrtEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "encryptionKey" in data:
        import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

        out["encryption_key"] = (
            aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["encryptionKey"]
            )
        )
    else:
        raise DeserializationError("SrtEncryptionConfiguration.encryption_key required")
    return out
