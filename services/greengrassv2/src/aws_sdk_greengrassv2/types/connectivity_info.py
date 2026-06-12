"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ConnectivityInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.port_number_int
    import aws_sdk_greengrassv2.types.string


class ConnectivityInfo(TypedDict):
    id: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>An ID for the connectivity information.</p>"""
    host_address: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The IP address or DNS address where client devices can connect to an MQTT broker on the Greengrass core device.</p>"""
    port_number: "aws_sdk_greengrassv2.types.port_number_int.PortNumberInt"
    """<p>The port where the MQTT broker operates on the core device. This port is typically 8883, which is the default port for the MQTT broker component that runs on core devices.</p>"""
    metadata: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>Additional metadata to provide to client devices that connect to this core device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityInfo) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "host_address" in value:
        out["HostAddress"] = value["host_address"]
    out["PortNumber"] = value.get("port_number", 0)
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> ConnectivityInfo:
    out: ConnectivityInfo = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "HostAddress" in data:
        out["host_address"] = data["HostAddress"]
    if "PortNumber" in data:
        out["port_number"] = data["PortNumber"]
    else:
        out["port_number"] = 0
    if "Metadata" in data:
        out["metadata"] = data["Metadata"]
    return out
