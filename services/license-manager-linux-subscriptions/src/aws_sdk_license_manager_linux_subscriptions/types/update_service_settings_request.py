"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#UpdateServiceSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery
    import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings


class UpdateServiceSettingsRequest(TypedDict, closed=True):
    linux_subscriptions_discovery: "aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery.LinuxSubscriptionsDiscovery"
    """<p>Describes if the discovery of Linux subscriptions is enabled.</p>"""
    linux_subscriptions_discovery_settings: "aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.LinuxSubscriptionsDiscoverySettings"
    """<p>The settings defined for Linux subscriptions discovery. The settings include if Organizations integration has been enabled, and which Regions data will be aggregated from.</p>"""
    allow_update: NotRequired["bool"]
    """<p>Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceSettingsRequest) -> dict:
    out: dict = {}
    out["LinuxSubscriptionsDiscovery"] = value["linux_subscriptions_discovery"]
    import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings

    out["LinuxSubscriptionsDiscoverySettings"] = (
        aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.serialize_json(
            value["linux_subscriptions_discovery_settings"]
        )
    )
    if "allow_update" in value:
        out["AllowUpdate"] = value["allow_update"]
    return out


def deserialize_json(data: dict) -> UpdateServiceSettingsRequest:
    out: UpdateServiceSettingsRequest = {}  # type: ignore[typeddict-item]
    if "LinuxSubscriptionsDiscovery" in data:
        out["linux_subscriptions_discovery"] = data["LinuxSubscriptionsDiscovery"]
    else:
        raise DeserializationError(
            "UpdateServiceSettingsRequest.linux_subscriptions_discovery required"
        )
    if "LinuxSubscriptionsDiscoverySettings" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings

        out["linux_subscriptions_discovery_settings"] = (
            aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.deserialize_json(
                data["LinuxSubscriptionsDiscoverySettings"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceSettingsRequest.linux_subscriptions_discovery_settings required"
        )
    if "AllowUpdate" in data:
        out["allow_update"] = data["AllowUpdate"]
    return out
