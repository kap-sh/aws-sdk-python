"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_virtual_interface

LocalGatewayVirtualInterfaceSet: TypeAlias = list[
    "capo_ec2.types.local_gateway_virtual_interface.LocalGatewayVirtualInterface"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayVirtualInterfaceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway_virtual_interface

        capo_ec2.types.local_gateway_virtual_interface.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayVirtualInterfaceSet:
    import capo_ec2.types.local_gateway_virtual_interface

    out: LocalGatewayVirtualInterfaceSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.local_gateway_virtual_interface.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LocalGatewayVirtualInterfaceSet:
    import capo_ec2.types.local_gateway_virtual_interface

    out: LocalGatewayVirtualInterfaceSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.local_gateway_virtual_interface.deserialize_ec2_query(child)
        )
    return out
