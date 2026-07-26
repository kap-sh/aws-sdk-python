"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateDirectConnectGatewayAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.direct_connect_gateway_attachment


class CreateDirectConnectGatewayAttachmentResponse(TypedDict, closed=True):
    direct_connect_gateway_attachment: NotRequired[
        "capo_networkmanager.types.direct_connect_gateway_attachment.DirectConnectGatewayAttachment"
    ]
    """<p>Describes the details of a <code>CreateDirectConnectGatewayAttachment</code> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDirectConnectGatewayAttachmentResponse) -> dict:
    out: dict = {}
    if "direct_connect_gateway_attachment" in value:
        import capo_networkmanager.types.direct_connect_gateway_attachment

        out["DirectConnectGatewayAttachment"] = (
            capo_networkmanager.types.direct_connect_gateway_attachment.serialize_json(
                value["direct_connect_gateway_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDirectConnectGatewayAttachmentResponse:
    out: CreateDirectConnectGatewayAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "DirectConnectGatewayAttachment" in data:
        import capo_networkmanager.types.direct_connect_gateway_attachment

        out["direct_connect_gateway_attachment"] = (
            capo_networkmanager.types.direct_connect_gateway_attachment.deserialize_json(
                data["DirectConnectGatewayAttachment"]
            )
        )
    return out
