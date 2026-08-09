"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateIpAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.ip_prefix_list
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.private_ip_address_string_list


class AssignPrivateIpAddressesRequest(TypedDict, closed=True):
    ipv4_prefixes: NotRequired["capo_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>One or more IPv4 prefixes assigned to the network interface. You can't use this option if you use the <code>Ipv4PrefixCount</code> option.</p>"""
    ipv4_prefix_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface. You can't use this option if you use the <code>Ipv4 Prefixes</code> option.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "capo_ec2.types.private_ip_address_string_list.PrivateIpAddressStringList"
    ]
    """<p>The IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this parameter when also specifying a number of secondary IP addresses.</p> <p>If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the subnet range.</p>"""
    secondary_private_ip_address_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also specifying private IP addresses.</p>"""
    allow_reassignment: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignPrivateIpAddressesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv4_prefixes" in value:
        import capo_ec2.types.ip_prefix_list

        capo_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{key_prefix}Ipv4Prefix"
        )
    if "ipv4_prefix_count" in value:
        pairs.append((f"{key_prefix}Ipv4PrefixCount", str(value["ipv4_prefix_count"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_addresses" in value:
        import capo_ec2.types.private_ip_address_string_list

        capo_ec2.types.private_ip_address_string_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddress"
        )
    if "secondary_private_ip_address_count" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryPrivateIpAddressCount",
                str(value["secondary_private_ip_address_count"]),
            )
        )
    if "allow_reassignment" in value:
        pairs.append(
            (
                f"{key_prefix}AllowReassignment",
                "true" if value["allow_reassignment"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> AssignPrivateIpAddressesRequest:
    out: AssignPrivateIpAddressesRequest = {}  # type: ignore[typeddict-item]
    child_ipv4_prefixes = el.find("Ipv4Prefix")
    if child_ipv4_prefixes is not None:
        import capo_ec2.types.ip_prefix_list

        out["ipv4_prefixes"] = capo_ec2.types.ip_prefix_list.deserialize_ec2_query(
            child_ipv4_prefixes
        )
    child_ipv4_prefix_count = el.find("Ipv4PrefixCount")
    if child_ipv4_prefix_count is not None:
        out["ipv4_prefix_count"] = int(child_ipv4_prefix_count.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip_addresses = el.find("privateIpAddress")
    if child_private_ip_addresses is not None:
        import capo_ec2.types.private_ip_address_string_list

        out["private_ip_addresses"] = (
            capo_ec2.types.private_ip_address_string_list.deserialize_ec2_query(
                child_private_ip_addresses
            )
        )
    child_secondary_private_ip_address_count = el.find("secondaryPrivateIpAddressCount")
    if child_secondary_private_ip_address_count is not None:
        out["secondary_private_ip_address_count"] = int(
            child_secondary_private_ip_address_count.text or ""
        )
    child_allow_reassignment = el.find("allowReassignment")
    if child_allow_reassignment is not None:
        out["allow_reassignment"] = (
            child_allow_reassignment.text or ""
        ).lower() == "true"
    return out
