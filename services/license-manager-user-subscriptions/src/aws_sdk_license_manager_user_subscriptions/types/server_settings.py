"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ServerSettings``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings


class _ServerSettings_RdsSalSettings(TypedDict):
    RdsSalSettings: "aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings.RdsSalSettings"


ServerSettings: TypeAlias = _ServerSettings_RdsSalSettings


# --- restJson1 ser/de ---
def serialize_json(value: ServerSettings) -> dict:
    if "RdsSalSettings" in value:
        import aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings

        return {
            "RdsSalSettings": aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings.serialize_json(
                value["RdsSalSettings"]
            )
        }
    else:
        raise SerializationError("ServerSettings: no variant present")


def deserialize_json(data: dict) -> ServerSettings:
    if "RdsSalSettings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings

        return {
            "RdsSalSettings": aws_sdk_license_manager_user_subscriptions.types.rds_sal_settings.deserialize_json(
                data["RdsSalSettings"]
            )
        }
    else:
        raise DeserializationError("ServerSettings: no recognized variant key")
