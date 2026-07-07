"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetDirectConnectGatewayAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.direct_connect_gateway_attachment


class GetDirectConnectGatewayAttachmentResponse(TypedDict, closed=True):
    direct_connect_gateway_attachment: NotRequired[
        "aws_sdk_networkmanager.types.direct_connect_gateway_attachment.DirectConnectGatewayAttachment"
    ]
    """<p>Shows details about the Direct Connect gateway attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDirectConnectGatewayAttachmentResponse) -> dict:
    out: dict = {}
    if "direct_connect_gateway_attachment" in value:
        import aws_sdk_networkmanager.types.direct_connect_gateway_attachment

        out["DirectConnectGatewayAttachment"] = (
            aws_sdk_networkmanager.types.direct_connect_gateway_attachment.serialize_json(
                value["direct_connect_gateway_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDirectConnectGatewayAttachmentResponse:
    out: GetDirectConnectGatewayAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "DirectConnectGatewayAttachment" in data:
        import aws_sdk_networkmanager.types.direct_connect_gateway_attachment

        out["direct_connect_gateway_attachment"] = (
            aws_sdk_networkmanager.types.direct_connect_gateway_attachment.deserialize_json(
                data["DirectConnectGatewayAttachment"]
            )
        )
    return out
