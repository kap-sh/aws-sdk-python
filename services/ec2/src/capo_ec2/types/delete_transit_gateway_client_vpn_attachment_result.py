"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayClientVpnAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_client_vpn_attachment


class DeleteTransitGatewayClientVpnAttachmentResult(TypedDict, closed=True):
    transit_gateway_client_vpn_attachment: NotRequired[
        "capo_ec2.types.transit_gateway_client_vpn_attachment.TransitGatewayClientVpnAttachment"
    ]
    """<p>Information about the Transit Gateway Client VPN attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayClientVpnAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_client_vpn_attachment" in value:
        import capo_ec2.types.transit_gateway_client_vpn_attachment

        capo_ec2.types.transit_gateway_client_vpn_attachment.serialize_ec2_query(
            value["transit_gateway_client_vpn_attachment"],
            pairs,
            f"{prefix}.TransitGatewayClientVpnAttachment",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayClientVpnAttachmentResult:
    out: DeleteTransitGatewayClientVpnAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_client_vpn_attachment = el.find(
        "TransitGatewayClientVpnAttachment"
    )
    if child_transit_gateway_client_vpn_attachment is not None:
        import capo_ec2.types.transit_gateway_client_vpn_attachment

        out["transit_gateway_client_vpn_attachment"] = (
            capo_ec2.types.transit_gateway_client_vpn_attachment.deserialize_ec2_query(
                child_transit_gateway_client_vpn_attachment
            )
        )
    return out
