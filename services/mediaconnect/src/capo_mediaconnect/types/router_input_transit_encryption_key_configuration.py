"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.automatic_encryption_key_configuration
    import capo_mediaconnect.types.secrets_manager_encryption_key_configuration


class _RouterInputTransitEncryptionKeyConfiguration_SecretsManager(
    TypedDict, closed=True
):
    SecretsManager: "capo_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"


class _RouterInputTransitEncryptionKeyConfiguration_Automatic(TypedDict, closed=True):
    Automatic: "capo_mediaconnect.types.automatic_encryption_key_configuration.AutomaticEncryptionKeyConfiguration"


RouterInputTransitEncryptionKeyConfiguration: TypeAlias = (
    _RouterInputTransitEncryptionKeyConfiguration_SecretsManager
    | _RouterInputTransitEncryptionKeyConfiguration_Automatic
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTransitEncryptionKeyConfiguration) -> dict:
    if "SecretsManager" in value:
        import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "secretsManager": capo_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
                value["SecretsManager"]
            )
        }
    elif "Automatic" in value:
        import capo_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "automatic": capo_mediaconnect.types.automatic_encryption_key_configuration.serialize_json(
                value["Automatic"]
            )
        }
    else:
        raise SerializationError(
            "RouterInputTransitEncryptionKeyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterInputTransitEncryptionKeyConfiguration:
    if "secretsManager" in data:
        import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "SecretsManager": capo_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["secretsManager"]
            )
        }
    elif "automatic" in data:
        import capo_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "Automatic": capo_mediaconnect.types.automatic_encryption_key_configuration.deserialize_json(
                data["automatic"]
            )
        }
    else:
        raise DeserializationError(
            "RouterInputTransitEncryptionKeyConfiguration: no recognized variant key"
        )
