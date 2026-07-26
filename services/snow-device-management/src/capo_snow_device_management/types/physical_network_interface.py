"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#PhysicalNetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snow_device_management.types.ip_address_assignment
    import capo_snow_device_management.types.physical_connector_type


class PhysicalNetworkInterface(TypedDict, closed=True):
    physical_network_interface_id: NotRequired["str"]
    """<p>The physical network interface ID.</p>"""
    physical_connector_type: NotRequired[
        "capo_snow_device_management.types.physical_connector_type.PhysicalConnectorType"
    ]
    """<p>The physical connector type.</p>"""
    ip_address_assignment: NotRequired[
        "capo_snow_device_management.types.ip_address_assignment.IpAddressAssignment"
    ]
    """<p>A value that describes whether the IP address is dynamic or persistent.</p>"""
    ip_address: NotRequired["str"]
    """<p>The IP address of the device.</p>"""
    netmask: NotRequired["str"]
    """<p>The netmask used to divide the IP address into subnets.</p>"""
    default_gateway: NotRequired["str"]
    """<p>The default gateway of the device.</p>"""
    mac_address: NotRequired["str"]
    """<p>The MAC address of the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalNetworkInterface) -> dict:
    out: dict = {}
    if "physical_network_interface_id" in value:
        out["physicalNetworkInterfaceId"] = value["physical_network_interface_id"]
    if "physical_connector_type" in value:
        out["physicalConnectorType"] = value["physical_connector_type"]
    if "ip_address_assignment" in value:
        out["ipAddressAssignment"] = value["ip_address_assignment"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "netmask" in value:
        out["netmask"] = value["netmask"]
    if "default_gateway" in value:
        out["defaultGateway"] = value["default_gateway"]
    if "mac_address" in value:
        out["macAddress"] = value["mac_address"]
    return out


def deserialize_json(data: dict) -> PhysicalNetworkInterface:
    out: PhysicalNetworkInterface = {}  # type: ignore[typeddict-item]
    if "physicalNetworkInterfaceId" in data:
        out["physical_network_interface_id"] = data["physicalNetworkInterfaceId"]
    if "physicalConnectorType" in data:
        out["physical_connector_type"] = data["physicalConnectorType"]
    if "ipAddressAssignment" in data:
        out["ip_address_assignment"] = data["ipAddressAssignment"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "netmask" in data:
        out["netmask"] = data["netmask"]
    if "defaultGateway" in data:
        out["default_gateway"] = data["defaultGateway"]
    if "macAddress" in data:
        out["mac_address"] = data["macAddress"]
    return out
