"""Generated from Smithy shape ``com.amazonaws.ec2#AssignIpv6AddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.ip_prefix_list
    import capo_ec2.types.ipv6_address_list
    import capo_ec2.types.network_interface_id


class AssignIpv6AddressesRequest(TypedDict, closed=True):
    ipv6_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface. You cannot use this option if you use the <code>Ipv6Prefixes</code> option.</p>"""
    ipv6_prefixes: NotRequired["capo_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>One or more IPv6 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv6PrefixCount</code> option.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    ipv6_addresses: NotRequired["capo_ec2.types.ipv6_address_list.Ipv6AddressList"]
    """<p>The IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of IPv6 addresses.</p>"""
    ipv6_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of additional IPv6 addresses to assign to the network interface. The specified number of IPv6 addresses are assigned in addition to the existing IPv6 addresses that are already assigned to the network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can't use this option if specifying specific IPv6 addresses.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignIpv6AddressesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv6_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv6PrefixCount", str(value["ipv6_prefix_count"])))
    if "ipv6_prefixes" in value:
        import capo_ec2.types.ip_prefix_list

        capo_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{key_prefix}Ipv6Prefixes"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "ipv6_addresses" in value:
        import capo_ec2.types.ipv6_address_list

        capo_ec2.types.ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{key_prefix}Ipv6Addresses"
        )
    if "ipv6_address_count" in value:
        pairs.append(
            (f"{key_prefix}Ipv6AddressCount", str(value["ipv6_address_count"]))
        )


def deserialize_ec2_query(el: Element) -> AssignIpv6AddressesRequest:
    out: AssignIpv6AddressesRequest = {}  # type: ignore[typeddict-item]
    child_ipv6_prefix_count = el.find("Ipv6PrefixCount")
    if child_ipv6_prefix_count is not None:
        out["ipv6_prefix_count"] = int(child_ipv6_prefix_count.text or "")
    if el.find("Ipv6Prefixes") is not None:
        import capo_ec2.types.ip_prefix_list

        out["ipv6_prefixes"] = capo_ec2.types.ip_prefix_list.deserialize_ec2_query(
            el, "Ipv6Prefixes"
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    if el.find("Ipv6Addresses") is not None:
        import capo_ec2.types.ipv6_address_list

        out["ipv6_addresses"] = capo_ec2.types.ipv6_address_list.deserialize_ec2_query(
            el, "Ipv6Addresses"
        )
    child_ipv6_address_count = el.find("Ipv6AddressCount")
    if child_ipv6_address_count is not None:
        out["ipv6_address_count"] = int(child_ipv6_address_count.text or "")
    return out
