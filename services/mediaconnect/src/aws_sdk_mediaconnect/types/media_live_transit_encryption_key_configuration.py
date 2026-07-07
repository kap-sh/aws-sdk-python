"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveTransitEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.automatic_encryption_key_configuration
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration


class _MediaLiveTransitEncryptionKeyConfiguration_SecretsManager(
    TypedDict, closed=True
):
    SecretsManager: "aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"


class _MediaLiveTransitEncryptionKeyConfiguration_Automatic(TypedDict, closed=True):
    Automatic: "aws_sdk_mediaconnect.types.automatic_encryption_key_configuration.AutomaticEncryptionKeyConfiguration"


MediaLiveTransitEncryptionKeyConfiguration: TypeAlias = (
    _MediaLiveTransitEncryptionKeyConfiguration_SecretsManager
    | _MediaLiveTransitEncryptionKeyConfiguration_Automatic
)


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveTransitEncryptionKeyConfiguration) -> dict:
    if "SecretsManager" in value:
        import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "secretsManager": aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
                value["SecretsManager"]
            )
        }
    elif "Automatic" in value:
        import aws_sdk_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "automatic": aws_sdk_mediaconnect.types.automatic_encryption_key_configuration.serialize_json(
                value["Automatic"]
            )
        }
    else:
        raise SerializationError(
            "MediaLiveTransitEncryptionKeyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MediaLiveTransitEncryptionKeyConfiguration:
    if "secretsManager" in data:
        import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "SecretsManager": aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["secretsManager"]
            )
        }
    elif "automatic" in data:
        import aws_sdk_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "Automatic": aws_sdk_mediaconnect.types.automatic_encryption_key_configuration.deserialize_json(
                data["automatic"]
            )
        }
    else:
        raise DeserializationError(
            "MediaLiveTransitEncryptionKeyConfiguration: no recognized variant key"
        )
