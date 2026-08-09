"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6AddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_prefix_list
    import capo_ec2.types.ipv6_address_list
    import capo_ec2.types.string


class UnassignIpv6AddressesResult(TypedDict, closed=True):
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    unassigned_ipv6_addresses: NotRequired[
        "capo_ec2.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 addresses that have been unassigned from the network interface.</p>"""
    unassigned_ipv6_prefixes: NotRequired["capo_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv6 prefixes that have been unassigned from the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnassignIpv6AddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "unassigned_ipv6_addresses" in value:
        import capo_ec2.types.ipv6_address_list

        capo_ec2.types.ipv6_address_list.serialize_ec2_query(
            value["unassigned_ipv6_addresses"],
            pairs,
            f"{key_prefix}UnassignedIpv6Addresses",
        )
    if "unassigned_ipv6_prefixes" in value:
        import capo_ec2.types.ip_prefix_list

        capo_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["unassigned_ipv6_prefixes"],
            pairs,
            f"{key_prefix}UnassignedIpv6PrefixSet",
        )


def deserialize_ec2_query(el: Element) -> UnassignIpv6AddressesResult:
    out: UnassignIpv6AddressesResult = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_unassigned_ipv6_addresses = el.find("unassignedIpv6Addresses")
    if child_unassigned_ipv6_addresses is not None:
        import capo_ec2.types.ipv6_address_list

        out["unassigned_ipv6_addresses"] = (
            capo_ec2.types.ipv6_address_list.deserialize_ec2_query(
                child_unassigned_ipv6_addresses
            )
        )
    child_unassigned_ipv6_prefixes = el.find("unassignedIpv6PrefixSet")
    if child_unassigned_ipv6_prefixes is not None:
        import capo_ec2.types.ip_prefix_list

        out["unassigned_ipv6_prefixes"] = (
            capo_ec2.types.ip_prefix_list.deserialize_ec2_query(
                child_unassigned_ipv6_prefixes
            )
        )
    return out
