"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IdentityProvider``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider

class _IdentityProvider_ActiveDirectoryIdentityProvider(TypedDict):
    ActiveDirectoryIdentityProvider: "aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider.ActiveDirectoryIdentityProvider"

IdentityProvider: TypeAlias = _IdentityProvider_ActiveDirectoryIdentityProvider

# --- restJson1 ser/de ---
def serialize_json(value: IdentityProvider) -> dict:
    if "ActiveDirectoryIdentityProvider" in value:
        import aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider
        return {"ActiveDirectoryIdentityProvider": aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider.serialize_json(value["ActiveDirectoryIdentityProvider"])}
    else:
        raise SerializationError("IdentityProvider: no variant present")


def deserialize_json(data: dict) -> IdentityProvider:
    if "ActiveDirectoryIdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider
        return {"ActiveDirectoryIdentityProvider": aws_sdk_license_manager_user_subscriptions.types.active_directory_identity_provider.deserialize_json(data["ActiveDirectoryIdentityProvider"])}
    else:
        raise DeserializationError("IdentityProvider: no recognized variant key")