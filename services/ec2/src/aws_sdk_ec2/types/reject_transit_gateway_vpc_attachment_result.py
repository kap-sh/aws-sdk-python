"""Generated from Smithy shape ``com.amazonaws.ec2#RejectTransitGatewayVpcAttachmentResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_vpc_attachment


class RejectTransitGatewayVpcAttachmentResult(TypedDict):
    transit_gateway_vpc_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_vpc_attachment.TransitGatewayVpcAttachment"
    ]
    """<p>Information about the attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RejectTransitGatewayVpcAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_vpc_attachment" in value:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment

        aws_sdk_ec2.types.transit_gateway_vpc_attachment.serialize_ec2_query(
            value["transit_gateway_vpc_attachment"],
            pairs,
            f"{prefix}.TransitGatewayVpcAttachment",
        )


def deserialize_ec2_query(el: Element) -> RejectTransitGatewayVpcAttachmentResult:
    out: RejectTransitGatewayVpcAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_vpc_attachment = el.find("TransitGatewayVpcAttachment")
    if child_transit_gateway_vpc_attachment is not None:
        import aws_sdk_ec2.types.transit_gateway_vpc_attachment

        out["transit_gateway_vpc_attachment"] = (
            aws_sdk_ec2.types.transit_gateway_vpc_attachment.deserialize_ec2_query(
                child_transit_gateway_vpc_attachment
            )
        )
    return out
