"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#LinuxSubscriptionsDiscoverySettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager_linux_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.organization_integration
    import aws_sdk_license_manager_linux_subscriptions.types.string_list


class LinuxSubscriptionsDiscoverySettings(TypedDict):
    source_regions: (
        "aws_sdk_license_manager_linux_subscriptions.types.string_list.StringList"
    )
    """<p>The Regions in which to discover data for Linux subscriptions.</p>"""
    organization_integration: "aws_sdk_license_manager_linux_subscriptions.types.organization_integration.OrganizationIntegration"
    """<p>Details if you have enabled resource discovery across your accounts in Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinuxSubscriptionsDiscoverySettings) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_linux_subscriptions.types.string_list

    out["SourceRegions"] = (
        aws_sdk_license_manager_linux_subscriptions.types.string_list.serialize_json(
            value["source_regions"]
        )
    )
    out["OrganizationIntegration"] = value["organization_integration"]
    return out


def deserialize_json(data: dict) -> LinuxSubscriptionsDiscoverySettings:
    out: LinuxSubscriptionsDiscoverySettings = {}  # type: ignore[typeddict-item]
    if "SourceRegions" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.string_list

        out["source_regions"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_list.deserialize_json(
                data["SourceRegions"]
            )
        )
    else:
        raise DeserializationError(
            "LinuxSubscriptionsDiscoverySettings.source_regions required"
        )
    if "OrganizationIntegration" in data:
        out["organization_integration"] = data["OrganizationIntegration"]
    else:
        raise DeserializationError(
            "LinuxSubscriptionsDiscoverySettings.organization_integration required"
        )
    return out
