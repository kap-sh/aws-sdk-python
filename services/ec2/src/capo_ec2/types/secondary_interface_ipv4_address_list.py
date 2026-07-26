"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceIpv4AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_interface_ipv4_address

SecondaryInterfaceIpv4AddressList: TypeAlias = list[
    "capo_ec2.types.secondary_interface_ipv4_address.SecondaryInterfaceIpv4Address"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryInterfaceIpv4AddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.secondary_interface_ipv4_address

        capo_ec2.types.secondary_interface_ipv4_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> SecondaryInterfaceIpv4AddressList:
    import capo_ec2.types.secondary_interface_ipv4_address

    out: SecondaryInterfaceIpv4AddressList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.secondary_interface_ipv4_address.deserialize_ec2_query(child)
        )
    return out
