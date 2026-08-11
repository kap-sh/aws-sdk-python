"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route_attachment

TransitGatewayRouteAttachmentList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_route_attachment.TransitGatewayRouteAttachment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteAttachmentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_route_attachment

        capo_ec2.types.transit_gateway_route_attachment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteAttachmentList:
    import capo_ec2.types.transit_gateway_route_attachment

    out: TransitGatewayRouteAttachmentList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_route_attachment.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayRouteAttachmentList:
    import capo_ec2.types.transit_gateway_route_attachment

    out: TransitGatewayRouteAttachmentList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_route_attachment.deserialize_ec2_query(child)
        )
    return out
