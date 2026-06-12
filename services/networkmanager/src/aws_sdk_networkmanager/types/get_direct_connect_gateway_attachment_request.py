"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetDirectConnectGatewayAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id


class GetDirectConnectGatewayAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the Direct Connect gateway attachment that you want to see details about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectConnectGatewayAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDirectConnectGatewayAttachmentRequest:
    out: GetDirectConnectGatewayAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
