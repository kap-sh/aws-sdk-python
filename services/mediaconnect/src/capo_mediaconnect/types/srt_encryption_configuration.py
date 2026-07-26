"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SrtEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.secrets_manager_encryption_key_configuration


class SrtEncryptionConfiguration(TypedDict, closed=True):
    encryption_key: "capo_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"
    """<p>Specifies the encryption key configuration used for encrypting SRT streams, including the key source and associated credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SrtEncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

    out["encryptionKey"] = (
        capo_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
            value["encryption_key"]
        )
    )
    return out


def deserialize_json(data: dict) -> SrtEncryptionConfiguration:
    out: SrtEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "encryptionKey" in data:
        import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

        out["encryption_key"] = (
            capo_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["encryptionKey"]
            )
        )
    else:
        raise DeserializationError("SrtEncryptionConfiguration.encryption_key required")
    return out
