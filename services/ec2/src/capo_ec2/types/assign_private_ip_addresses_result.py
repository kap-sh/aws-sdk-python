"""Generated from Smithy shape ``com.amazonaws.ec2#AssignPrivateIpAddressesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.assigned_private_ip_address_list
    import capo_ec2.types.ipv4_prefixes_list
    import capo_ec2.types.string


class AssignPrivateIpAddressesResult(TypedDict, closed=True):
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    assigned_private_ip_addresses: NotRequired[
        "capo_ec2.types.assigned_private_ip_address_list.AssignedPrivateIpAddressList"
    ]
    """<p>The private IP addresses assigned to the network interface.</p>"""
    assigned_ipv4_prefixes: NotRequired[
        "capo_ec2.types.ipv4_prefixes_list.Ipv4PrefixesList"
    ]
    """<p>The IPv4 prefixes that are assigned to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignPrivateIpAddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "assigned_private_ip_addresses" in value:
        import capo_ec2.types.assigned_private_ip_address_list

        capo_ec2.types.assigned_private_ip_address_list.serialize_ec2_query(
            value["assigned_private_ip_addresses"],
            pairs,
            f"{key_prefix}AssignedPrivateIpAddressesSet",
        )
    if "assigned_ipv4_prefixes" in value:
        import capo_ec2.types.ipv4_prefixes_list

        capo_ec2.types.ipv4_prefixes_list.serialize_ec2_query(
            value["assigned_ipv4_prefixes"], pairs, f"{key_prefix}AssignedIpv4PrefixSet"
        )


def deserialize_ec2_query(el: Element) -> AssignPrivateIpAddressesResult:
    out: AssignPrivateIpAddressesResult = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    if el.find("AssignedPrivateIpAddressesSet") is not None:
        import capo_ec2.types.assigned_private_ip_address_list

        out["assigned_private_ip_addresses"] = (
            capo_ec2.types.assigned_private_ip_address_list.deserialize_ec2_query(
                el, "AssignedPrivateIpAddressesSet"
            )
        )
    if el.find("AssignedIpv4PrefixSet") is not None:
        import capo_ec2.types.ipv4_prefixes_list

        out["assigned_ipv4_prefixes"] = (
            capo_ec2.types.ipv4_prefixes_list.deserialize_ec2_query(
                el, "AssignedIpv4PrefixSet"
            )
        )
    return out
