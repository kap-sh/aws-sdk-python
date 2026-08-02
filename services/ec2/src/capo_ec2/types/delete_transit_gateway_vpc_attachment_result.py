"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayVpcAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_vpc_attachment


class DeleteTransitGatewayVpcAttachmentResult(TypedDict, closed=True):
    transit_gateway_vpc_attachment: NotRequired[
        "capo_ec2.types.transit_gateway_vpc_attachment.TransitGatewayVpcAttachment"
    ]
    """<p>Information about the deleted VPC attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayVpcAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_vpc_attachment" in value:
        import capo_ec2.types.transit_gateway_vpc_attachment

        capo_ec2.types.transit_gateway_vpc_attachment.serialize_ec2_query(
            value["transit_gateway_vpc_attachment"],
            pairs,
            f"{key_prefix}TransitGatewayVpcAttachment",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayVpcAttachmentResult:
    out: DeleteTransitGatewayVpcAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_vpc_attachment = el.find("TransitGatewayVpcAttachment")
    if child_transit_gateway_vpc_attachment is not None:
        import capo_ec2.types.transit_gateway_vpc_attachment

        out["transit_gateway_vpc_attachment"] = (
            capo_ec2.types.transit_gateway_vpc_attachment.deserialize_ec2_query(
                child_transit_gateway_vpc_attachment
            )
        )
    return out
