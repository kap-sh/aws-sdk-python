"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPeeringAttachmentList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_peering_attachment

TransitGatewayPeeringAttachmentList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_peering_attachment.TransitGatewayPeeringAttachment"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayPeeringAttachmentList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_peering_attachment

        aws_sdk_ec2.types.transit_gateway_peering_attachment.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayPeeringAttachmentList:
    import aws_sdk_ec2.types.transit_gateway_peering_attachment

    out: TransitGatewayPeeringAttachmentList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_peering_attachment.deserialize_ec2_query(
                child
            )
        )
    return out
