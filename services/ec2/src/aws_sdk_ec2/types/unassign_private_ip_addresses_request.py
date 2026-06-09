"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateIpAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_prefix_list
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.private_ip_address_string_list


class UnassignPrivateIpAddressesRequest(TypedDict):
    ipv4_prefixes: NotRequired["aws_sdk_ec2.types.ip_prefix_list.IpPrefixList"]
    """<p>The IPv4 prefixes to unassign from the network interface.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    private_ip_addresses: NotRequired[
        "aws_sdk_ec2.types.private_ip_address_string_list.PrivateIpAddressStringList"
    ]
    """<p>The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnassignPrivateIpAddressesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv4_prefixes" in value:
        import aws_sdk_ec2.types.ip_prefix_list

        aws_sdk_ec2.types.ip_prefix_list.serialize_ec2_query(
            value["ipv4_prefixes"], pairs, f"{prefix}.Ipv4Prefixes"
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip_addresses" in value:
        import aws_sdk_ec2.types.private_ip_address_string_list

        aws_sdk_ec2.types.private_ip_address_string_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{prefix}.PrivateIpAddress"
        )


def deserialize_ec2_query(el: Element) -> UnassignPrivateIpAddressesRequest:
    out: UnassignPrivateIpAddressesRequest = {}  # type: ignore[typeddict-item]
    if el.find("Ipv4Prefixes") is not None:
        import aws_sdk_ec2.types.ip_prefix_list

        out["ipv4_prefixes"] = aws_sdk_ec2.types.ip_prefix_list.deserialize_ec2_query(
            el, "Ipv4Prefixes"
        )
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    if el.find("PrivateIpAddress") is not None:
        import aws_sdk_ec2.types.private_ip_address_string_list

        out["private_ip_addresses"] = (
            aws_sdk_ec2.types.private_ip_address_string_list.deserialize_ec2_query(
                el, "PrivateIpAddress"
            )
        )
    return out
