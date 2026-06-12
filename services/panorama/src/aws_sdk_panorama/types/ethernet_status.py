"""Generated from Smithy shape ``com.amazonaws.panorama#EthernetStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.hw_address
    import aws_sdk_panorama.types.ip_address
    import aws_sdk_panorama.types.network_connection_status


class EthernetStatus(TypedDict):
    ip_address: NotRequired["aws_sdk_panorama.types.ip_address.IpAddress"]
    """<p>The device's IP address.</p>"""
    connection_status: NotRequired[
        "aws_sdk_panorama.types.network_connection_status.NetworkConnectionStatus"
    ]
    """<p>The device's connection status.</p>"""
    hw_address: NotRequired["aws_sdk_panorama.types.hw_address.HwAddress"]
    """<p>The device's physical address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EthernetStatus) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "connection_status" in value:
        out["ConnectionStatus"] = value["connection_status"]
    if "hw_address" in value:
        out["HwAddress"] = value["hw_address"]
    return out


def deserialize_json(data: dict) -> EthernetStatus:
    out: EthernetStatus = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "ConnectionStatus" in data:
        out["connection_status"] = data["ConnectionStatus"]
    if "HwAddress" in data:
        out["hw_address"] = data["HwAddress"]
    return out
