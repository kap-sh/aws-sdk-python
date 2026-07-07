"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.server_settings
    import aws_sdk_license_manager_user_subscriptions.types.server_type


class LicenseServerSettings(TypedDict, closed=True):
    server_type: (
        "aws_sdk_license_manager_user_subscriptions.types.server_type.ServerType"
    )
    """<p>The type of license server.</p>"""
    server_settings: "aws_sdk_license_manager_user_subscriptions.types.server_settings.ServerSettings"
    """<p>The <code>ServerSettings</code> resource contains the settings for your server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServerSettings) -> dict:
    out: dict = {}
    out["ServerType"] = value["server_type"]
    import aws_sdk_license_manager_user_subscriptions.types.server_settings

    out["ServerSettings"] = (
        aws_sdk_license_manager_user_subscriptions.types.server_settings.serialize_json(
            value["server_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> LicenseServerSettings:
    out: LicenseServerSettings = {}  # type: ignore[typeddict-item]
    if "ServerType" in data:
        out["server_type"] = data["ServerType"]
    else:
        raise DeserializationError("LicenseServerSettings.server_type required")
    if "ServerSettings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.server_settings

        out["server_settings"] = (
            aws_sdk_license_manager_user_subscriptions.types.server_settings.deserialize_json(
                data["ServerSettings"]
            )
        )
    else:
        raise DeserializationError("LicenseServerSettings.server_settings required")
    return out
