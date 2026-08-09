"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route

LocalGatewayRouteList: TypeAlias = list[
    "capo_ec2.types.local_gateway_route.LocalGatewayRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway_route

        capo_ec2.types.local_gateway_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteList:
    import capo_ec2.types.local_gateway_route

    out: LocalGatewayRouteList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.local_gateway_route.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> LocalGatewayRouteList:
    import capo_ec2.types.local_gateway_route

    out: LocalGatewayRouteList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.local_gateway_route.deserialize_ec2_query(child))
    return out
