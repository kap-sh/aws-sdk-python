"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtDecryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration


class SrtDecryptionConfiguration(TypedDict, closed=True):
    encryption_key: "aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"
    """<p>Specifies the encryption key configuration used for decrypting SRT streams, including the key source and associated credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtDecryptionConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

    out["encryptionKey"] = (
        aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
            value["encryption_key"]
        )
    )
    return out


def deserialize_json(data: dict) -> SrtDecryptionConfiguration:
    out: SrtDecryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "encryptionKey" in data:
        import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

        out["encryption_key"] = (
            aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["encryptionKey"]
            )
        )
    else:
        raise DeserializationError("SrtDecryptionConfiguration.encryption_key required")
    return out
