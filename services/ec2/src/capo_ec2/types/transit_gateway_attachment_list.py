"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_attachment

TransitGatewayAttachmentList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_attachment.TransitGatewayAttachment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_attachment

        capo_ec2.types.transit_gateway_attachment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentList:
    import capo_ec2.types.transit_gateway_attachment

    out: TransitGatewayAttachmentList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_attachment.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayAttachmentList:
    import capo_ec2.types.transit_gateway_attachment

    out: TransitGatewayAttachmentList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_attachment.deserialize_ec2_query(child)
        )
    return out
