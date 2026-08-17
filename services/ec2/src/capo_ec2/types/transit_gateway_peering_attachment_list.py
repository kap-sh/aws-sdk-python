"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_peering_attachment

TransitGatewayPeeringAttachmentList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_peering_attachment.TransitGatewayPeeringAttachment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPeeringAttachmentList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_peering_attachment

        capo_ec2.types.transit_gateway_peering_attachment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayPeeringAttachmentList:
    import capo_ec2.types.transit_gateway_peering_attachment

    out: TransitGatewayPeeringAttachmentList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_peering_attachment.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayPeeringAttachmentList:
    import capo_ec2.types.transit_gateway_peering_attachment

    out: TransitGatewayPeeringAttachmentList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_peering_attachment.deserialize_ec2_query(
                child
            )
        )
    return out
