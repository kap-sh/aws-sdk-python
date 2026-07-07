"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#UpdateServiceSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery
    import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings
    import aws_sdk_license_manager_linux_subscriptions.types.status
    import aws_sdk_license_manager_linux_subscriptions.types.string_list
    import aws_sdk_license_manager_linux_subscriptions.types.string_map


class UpdateServiceSettingsResponse(TypedDict, closed=True):
    linux_subscriptions_discovery: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery.LinuxSubscriptionsDiscovery"
    ]
    """<p>Lists if discovery has been enabled for Linux subscriptions.</p>"""
    linux_subscriptions_discovery_settings: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.LinuxSubscriptionsDiscoverySettings"
    ]
    """<p>The settings defined for Linux subscriptions discovery. The settings include if Organizations integration has been enabled, and which Regions data will be aggregated from.</p>"""
    status: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.status.Status"
    ]
    """<p>Indicates the status of Linux subscriptions settings being applied.</p>"""
    status_message: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.string_map.StringMap"
    ]
    """<p>A message which details the Linux subscriptions service settings current status.</p>"""
    home_regions: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.string_list.StringList"
    ]
    """<p>The Region in which License Manager displays the aggregated data for Linux subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServiceSettingsResponse) -> dict:
    out: dict = {}
    if "linux_subscriptions_discovery" in value:
        out["LinuxSubscriptionsDiscovery"] = value["linux_subscriptions_discovery"]
    if "linux_subscriptions_discovery_settings" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings

        out["LinuxSubscriptionsDiscoverySettings"] = (
            aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.serialize_json(
                value["linux_subscriptions_discovery_settings"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.string_map

        out["StatusMessage"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_map.serialize_json(
                value["status_message"]
            )
        )
    if "home_regions" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.string_list

        out["HomeRegions"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_list.serialize_json(
                value["home_regions"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServiceSettingsResponse:
    out: UpdateServiceSettingsResponse = {}  # type: ignore[typeddict-item]
    if "LinuxSubscriptionsDiscovery" in data:
        out["linux_subscriptions_discovery"] = data["LinuxSubscriptionsDiscovery"]
    if "LinuxSubscriptionsDiscoverySettings" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings

        out["linux_subscriptions_discovery_settings"] = (
            aws_sdk_license_manager_linux_subscriptions.types.linux_subscriptions_discovery_settings.deserialize_json(
                data["LinuxSubscriptionsDiscoverySettings"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusMessage" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.string_map

        out["status_message"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_map.deserialize_json(
                data["StatusMessage"]
            )
        )
    if "HomeRegions" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.string_list

        out["home_regions"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_list.deserialize_json(
                data["HomeRegions"]
            )
        )
    return out
