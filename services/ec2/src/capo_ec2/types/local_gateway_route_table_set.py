"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table

LocalGatewayRouteTableSet: TypeAlias = list[
    "capo_ec2.types.local_gateway_route_table.LocalGatewayRouteTable"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTableSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway_route_table

        capo_ec2.types.local_gateway_route_table.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteTableSet:
    import capo_ec2.types.local_gateway_route_table

    out: LocalGatewayRouteTableSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.local_gateway_route_table.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LocalGatewayRouteTableSet:
    import capo_ec2.types.local_gateway_route_table

    out: LocalGatewayRouteTableSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.local_gateway_route_table.deserialize_ec2_query(child)
        )
    return out
