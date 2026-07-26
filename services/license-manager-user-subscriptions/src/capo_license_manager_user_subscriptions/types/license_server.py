"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#LicenseServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.license_server_endpoint_provisioning_status
    import capo_license_manager_user_subscriptions.types.license_server_health_status


class LicenseServer(TypedDict, closed=True):
    provisioning_status: NotRequired[
        "capo_license_manager_user_subscriptions.types.license_server_endpoint_provisioning_status.LicenseServerEndpointProvisioningStatus"
    ]
    """<p>The current state of the provisioning process for the RDS license server.</p>"""
    health_status: NotRequired[
        "capo_license_manager_user_subscriptions.types.license_server_health_status.LicenseServerHealthStatus"
    ]
    """<p>The health status of the RDS license server.</p>"""
    ipv4_address: NotRequired["str"]
    """<p>A list of domain IPv4 addresses that are used for the RDS license server.</p>"""
    ipv6_address: NotRequired["str"]
    """<p>A list of domain IPv6 addresses that are used for the RDS license server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseServer) -> dict:
    out: dict = {}
    if "provisioning_status" in value:
        out["ProvisioningStatus"] = value["provisioning_status"]
    if "health_status" in value:
        out["HealthStatus"] = value["health_status"]
    if "ipv4_address" in value:
        out["Ipv4Address"] = value["ipv4_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    return out


def deserialize_json(data: dict) -> LicenseServer:
    out: LicenseServer = {}  # type: ignore[typeddict-item]
    if "ProvisioningStatus" in data:
        out["provisioning_status"] = data["ProvisioningStatus"]
    if "HealthStatus" in data:
        out["health_status"] = data["HealthStatus"]
    if "Ipv4Address" in data:
        out["ipv4_address"] = data["Ipv4Address"]
    if "Ipv6Address" in data:
        out["ipv6_address"] = data["Ipv6Address"]
    return out
