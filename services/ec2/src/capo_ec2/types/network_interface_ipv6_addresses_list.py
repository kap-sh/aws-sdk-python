"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIpv6AddressesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_ipv6_address

NetworkInterfaceIpv6AddressesList: TypeAlias = list[
    "capo_ec2.types.network_interface_ipv6_address.NetworkInterfaceIpv6Address"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfaceIpv6AddressesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.network_interface_ipv6_address

        capo_ec2.types.network_interface_ipv6_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> NetworkInterfaceIpv6AddressesList:
    import capo_ec2.types.network_interface_ipv6_address

    out: NetworkInterfaceIpv6AddressesList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.network_interface_ipv6_address.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> NetworkInterfaceIpv6AddressesList:
    import capo_ec2.types.network_interface_ipv6_address

    out: NetworkInterfaceIpv6AddressesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.network_interface_ipv6_address.deserialize_ec2_query(child)
        )
    return out
