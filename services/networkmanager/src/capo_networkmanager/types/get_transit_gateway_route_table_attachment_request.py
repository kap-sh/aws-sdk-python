"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRouteTableAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id


class GetTransitGatewayRouteTableAttachmentRequest(TypedDict, closed=True):
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the transit gateway route table attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRouteTableAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRouteTableAttachmentRequest:
    out: GetTransitGatewayRouteTableAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
