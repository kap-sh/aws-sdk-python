"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#SocketAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.port_number


class SocketAddress(TypedDict, closed=True):
    ip_address: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The IP address for the socket address.</p>"""
    port: NotRequired["aws_sdk_global_accelerator.types.port_number.PortNumber"]
    """<p>The port for the socket address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SocketAddress) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SocketAddress:
    out: SocketAddress = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "Port" in data:
        out["port"] = data["Port"]
    return out
