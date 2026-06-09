"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignIpv6AddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.ipv6_address_list
    import aws_sdk_ec2.types.network_interface_id


class UnassignIpv6AddressesRequest(TypedDict):
    ipv6_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv6 prefixes to unassign from the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    ipv6_addresses: NotRequired["aws_sdk_ec2.types.ipv6_address_list.Ipv6AddressList"]
    """<p>The IPv6 addresses to unassign from the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnassignIpv6AddressesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_prefixes" in value:
        import aws_sdk_ec2.types.ip_prefix_list

        aws_sdk_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["ipv6_prefixes"], pairs, f"{prefix}.Ipv6Prefixes"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "ipv6_addresses" in value:
        import aws_sdk_ec2.types.ipv6_address_list

        aws_sdk_ec2.types.ipv6_address_list.serialize_ec2_query(
            value["ipv6_addresses"], pairs, f"{prefix}.Ipv6Addresses"
        )


def deserialize_ec2_query(el: Element) -> UnassignIpv6AddressesRequest:
    out: UnassignIpv6AddressesRequest = {}  # type: ignore[typeddict-item]
    if el.find("Ipv6Prefixes") is not None:
        import aws_sdk_ec2.types.ip_prefix_list

        out["ipv6_prefixes"] = aws_sdk_ec2.types.ip_prefix_list.deserialize_ec2_query(
            el, "Ipv6Prefixes"
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    if el.find("Ipv6Addresses") is not None:
        import aws_sdk_ec2.types.ipv6_address_list

        out["ipv6_addresses"] = (
            aws_sdk_ec2.types.ipv6_address_list.deserialize_ec2_query(
                el, "Ipv6Addresses"
            )
        )
    return out
