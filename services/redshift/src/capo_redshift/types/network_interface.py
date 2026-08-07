"""Generated from Smithy shape ``com.amazonaws.redshift#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class NetworkInterface(TypedDict, closed=True):
    network_interface_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The network interface identifier. </p>"""
    subnet_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The subnet identifier. </p>"""
    private_ip_address: NotRequired["capo_redshift.types.string.String"]
    """<p>The IPv4 address of the network interface within the subnet. </p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The Availability Zone. </p>"""
    ipv6_address: NotRequired["capo_redshift.types.string.String"]
    """<p>The IPv6 address of the network interface within the subnet. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "ipv6_address" in value:
        pairs.append((f"{key_prefix}Ipv6Address", str(value["ipv6_address"])))


def deserialize_query(el: Element) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_ipv6_address = el.find("Ipv6Address")
    if child_ipv6_address is not None:
        out["ipv6_address"] = str(child_ipv6_address.text or "")
    return out
