"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route_table

TransitGatewayRouteTableList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_route_table.TransitGatewayRouteTable"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTableList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_route_table

        capo_ec2.types.transit_gateway_route_table.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableList:
    import capo_ec2.types.transit_gateway_route_table

    out: TransitGatewayRouteTableList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_route_table.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayRouteTableList:
    import capo_ec2.types.transit_gateway_route_table

    out: TransitGatewayRouteTableList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_route_table.deserialize_ec2_query(child)
        )
    return out
