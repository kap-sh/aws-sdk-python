"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#CredentialsProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider


class _CredentialsProvider_SecretsManagerCredentialsProvider(TypedDict, closed=True):
    SecretsManagerCredentialsProvider: "aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.SecretsManagerCredentialsProvider"


CredentialsProvider: TypeAlias = _CredentialsProvider_SecretsManagerCredentialsProvider


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsProvider) -> dict:
    if "SecretsManagerCredentialsProvider" in value:
        import aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider

        return {
            "SecretsManagerCredentialsProvider": aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.serialize_json(
                value["SecretsManagerCredentialsProvider"]
            )
        }
    else:
        raise SerializationError("CredentialsProvider: no variant present")


def deserialize_json(data: dict) -> CredentialsProvider:
    if "SecretsManagerCredentialsProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider

        return {
            "SecretsManagerCredentialsProvider": aws_sdk_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.deserialize_json(
                data["SecretsManagerCredentialsProvider"]
            )
        }
    else:
        raise DeserializationError("CredentialsProvider: no recognized variant key")
