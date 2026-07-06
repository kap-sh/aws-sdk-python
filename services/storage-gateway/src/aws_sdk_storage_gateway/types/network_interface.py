"""Generated from Smithy shape ``com.amazonaws.storagegateway#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.string


class NetworkInterface(TypedDict, closed=True):
    ipv4_address: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The Internet Protocol version 4 (IPv4) address of the interface.</p>"""
    mac_address: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The Media Access Control (MAC) address of the interface.</p> <note> <p>This is currently unsupported and will not be returned in output.</p> </note>"""
    ipv6_address: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The Internet Protocol version 6 (IPv6) address of the interface.</p> <note> <p>This element returns IPv6 addresses for all gateway types except FSx File Gateway.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterface) -> dict:
    out: dict = {}
    if "ipv4_address" in value:
        out["Ipv4Address"] = value["ipv4_address"]
    if "mac_address" in value:
        out["MacAddress"] = value["mac_address"]
    if "ipv6_address" in value:
        out["Ipv6Address"] = value["ipv6_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "Ipv4Address" in data:
        out["ipv4_address"] = data["Ipv4Address"]
    if "MacAddress" in data:
        out["mac_address"] = data["MacAddress"]
    if "Ipv6Address" in data:
        out["ipv6_address"] = data["Ipv6Address"]
    return out
