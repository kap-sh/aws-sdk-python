"""Generated from Smithy shape ``com.amazonaws.ec2#AssignIpv6AddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_prefix_list
    import capo_ec2.types.ipv6_address_list
    import capo_ec2.types.string


class AssignIpv6AddressesResult(TypedDict, closed=True):
    assigned_ipv6_addresses: NotRequired[
        "capo_ec2.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The new IPv6 addresses assigned to the network interface. Existing IPv6 addresses that were assigned to the network interface before the request are not included.</p>"""
    assigned_ipv6_prefixes: NotRequired["capo_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv6 prefixes that are assigned to the network interface.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignIpv6AddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "assigned_ipv6_addresses" in value:
        import capo_ec2.types.ipv6_address_list

        capo_ec2.types.ipv6_address_list.serialize_ec2_query(
            value["assigned_ipv6_addresses"], pairs, f"{prefix}.AssignedIpv6Addresses"
        )
    if "assigned_ipv6_prefixes" in value:
        import capo_ec2.types.ip_prefix_list

        capo_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["assigned_ipv6_prefixes"], pairs, f"{prefix}.AssignedIpv6PrefixSet"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )


def deserialize_ec2_query(el: Element) -> AssignIpv6AddressesResult:
    out: AssignIpv6AddressesResult = {}  # type: ignore[typeddict-item]
    if el.find("AssignedIpv6Addresses") is not None:
        import capo_ec2.types.ipv6_address_list

        out["assigned_ipv6_addresses"] = (
            capo_ec2.types.ipv6_address_list.deserialize_ec2_query(
                el, "AssignedIpv6Addresses"
            )
        )
    if el.find("AssignedIpv6PrefixSet") is not None:
        import capo_ec2.types.ip_prefix_list

        out["assigned_ipv6_prefixes"] = (
            capo_ec2.types.ip_prefix_list.deserialize_ec2_query(
                el, "AssignedIpv6PrefixSet"
            )
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    return out
