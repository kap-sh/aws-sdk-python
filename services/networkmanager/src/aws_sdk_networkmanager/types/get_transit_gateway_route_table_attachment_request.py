"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRouteTableAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id


class GetTransitGatewayRouteTableAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the transit gateway route table attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRouteTableAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRouteTableAttachmentRequest:
    out: GetTransitGatewayRouteTableAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
