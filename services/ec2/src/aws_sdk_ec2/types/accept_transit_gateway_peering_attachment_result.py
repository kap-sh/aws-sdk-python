"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptTransitGatewayPeeringAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_peering_attachment


class AcceptTransitGatewayPeeringAttachmentResult(TypedDict, closed=True):
    transit_gateway_peering_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_peering_attachment.TransitGatewayPeeringAttachment"
    ]
    """<p>The transit gateway peering attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptTransitGatewayPeeringAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_peering_attachment" in value:
        import aws_sdk_ec2.types.transit_gateway_peering_attachment

        aws_sdk_ec2.types.transit_gateway_peering_attachment.serialize_ec2_query(
            value["transit_gateway_peering_attachment"],
            pairs,
            f"{prefix}.TransitGatewayPeeringAttachment",
        )


def deserialize_ec2_query(el: Element) -> AcceptTransitGatewayPeeringAttachmentResult:
    out: AcceptTransitGatewayPeeringAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_peering_attachment = el.find(
        "TransitGatewayPeeringAttachment"
    )
    if child_transit_gateway_peering_attachment is not None:
        import aws_sdk_ec2.types.transit_gateway_peering_attachment

        out["transit_gateway_peering_attachment"] = (
            aws_sdk_ec2.types.transit_gateway_peering_attachment.deserialize_ec2_query(
                child_transit_gateway_peering_attachment
            )
        )
    return out
