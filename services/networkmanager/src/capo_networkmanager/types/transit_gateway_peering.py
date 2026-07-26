"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayPeering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.peering
    import capo_networkmanager.types.transit_gateway_arn
    import capo_networkmanager.types.transit_gateway_peering_attachment_id


class TransitGatewayPeering(TypedDict, closed=True):
    peering: NotRequired["capo_networkmanager.types.peering.Peering"]
    """<p>Describes a transit gateway peer connection.</p>"""
    transit_gateway_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    ]
    """<p>The ARN of the transit gateway.</p>"""
    transit_gateway_peering_attachment_id: NotRequired[
        "capo_networkmanager.types.transit_gateway_peering_attachment_id.TransitGatewayPeeringAttachmentId"
    ]
    """<p>The ID of the transit gateway peering attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayPeering) -> dict:
    out: dict = {}
    if "peering" in value:
        import capo_networkmanager.types.peering

        out["Peering"] = capo_networkmanager.types.peering.serialize_json(
            value["peering"]
        )
    if "transit_gateway_arn" in value:
        out["TransitGatewayArn"] = value["transit_gateway_arn"]
    if "transit_gateway_peering_attachment_id" in value:
        out["TransitGatewayPeeringAttachmentId"] = value[
            "transit_gateway_peering_attachment_id"
        ]
    return out


def deserialize_json(data: dict) -> TransitGatewayPeering:
    out: TransitGatewayPeering = {}  # type: ignore[typeddict-item]
    if "Peering" in data:
        import capo_networkmanager.types.peering

        out["peering"] = capo_networkmanager.types.peering.deserialize_json(
            data["Peering"]
        )
    if "TransitGatewayArn" in data:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    if "TransitGatewayPeeringAttachmentId" in data:
        out["transit_gateway_peering_attachment_id"] = data[
            "TransitGatewayPeeringAttachmentId"
        ]
    return out
