"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6AddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.string


class UnassignIpv6AddressesResult(TypedDict):
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    unassigned_ipv6_addresses: NotRequired[
        "aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"
    ]
    """<p>The IPv6 addresses that have been unassigned from the network interface.</p>"""
    unassigned_ipv6_prefixes: NotRequired[
        "aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"
    ]
    """<p>The IPv6 prefixes that have been unassigned from the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnassignIpv6AddressesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "unassigned_ipv6_addresses" in value:
        import aws_sdk_ec2.types.ipv6_address_list

        aws_sdk_ec2.types.ipv6_address_list.serialize_ec2_query(
            value["unassigned_ipv6_addresses"],
            pairs,
            f"{prefix}.UnassignedIpv6Addresses",
        )
    if "unassigned_ipv6_prefixes" in value:
        import aws_sdk_ec2.types.ip_prefix_list

        aws_sdk_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["unassigned_ipv6_prefixes"],
            pairs,
            f"{prefix}.UnassignedIpv6PrefixSet",
        )


def deserialize_ec2_query(el: Element) -> UnassignIpv6AddressesResult:
    out: UnassignIpv6AddressesResult = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    if el.find("UnassignedIpv6Addresses") is not None:
        import aws_sdk_ec2.types.ipv6_address_list

        out["unassigned_ipv6_addresses"] = (
            aws_sdk_ec2.types.ipv6_address_list.deserialize_ec2_query(
                el, "UnassignedIpv6Addresses"
            )
        )
    if el.find("UnassignedIpv6PrefixSet") is not None:
        import aws_sdk_ec2.types.ip_prefix_list

        out["unassigned_ipv6_prefixes"] = (
            aws_sdk_ec2.types.ip_prefix_list.deserialize_ec2_query(
                el, "UnassignedIpv6PrefixSet"
            )
        )
    return out
