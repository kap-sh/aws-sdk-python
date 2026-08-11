"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAnnouncementList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route_table_announcement

TransitGatewayRouteTableAnnouncementList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_route_table_announcement.TransitGatewayRouteTableAnnouncement"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayRouteTableAnnouncementList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_route_table_announcement

        capo_ec2.types.transit_gateway_route_table_announcement.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayRouteTableAnnouncementList:
    import capo_ec2.types.transit_gateway_route_table_announcement

    out: TransitGatewayRouteTableAnnouncementList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_route_table_announcement.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayRouteTableAnnouncementList:
    import capo_ec2.types.transit_gateway_route_table_announcement

    out: TransitGatewayRouteTableAnnouncementList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_route_table_announcement.deserialize_ec2_query(
                child
            )
        )
    return out
