"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FlowTransitEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.automatic_encryption_key_configuration
    import aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration


class _FlowTransitEncryptionKeyConfiguration_SecretsManager(TypedDict, closed=True):
    SecretsManager: "aws_sdk_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"


class _FlowTransitEncryptionKeyConfiguration_Automatic(TypedDict, closed=True):
    Automatic: "aws_sdk_mediaconnect.types.automatic_encryption_key_configuration.AutomaticEncryptionKeyConfiguration"


FlowTransitEncryptionKeyConfiguration: TypeAlias = (
    _FlowTransitEncryptionKeyConfiguration_SecretsManager
    | _FlowTransitEncryptionKeyConfiguration_Automatic
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowTransitEncryptionKeyConfiguration) -> dict:
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
            "FlowTransitEncryptionKeyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> FlowTransitEncryptionKeyConfiguration:
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
            "FlowTransitEncryptionKeyConfiguration: no recognized variant key"
        )
