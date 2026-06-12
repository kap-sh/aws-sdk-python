"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayPeeringRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering_id


class GetTransitGatewayPeeringRequest(TypedDict):
    peering_id: "aws_sdk_networkmanager.types.peering_id.PeeringId"
    """<p>The ID of the peering request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayPeeringRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTransitGatewayPeeringRequest:
    out: GetTransitGatewayPeeringRequest = {}  # type: ignore[typeddict-item]
    return out
