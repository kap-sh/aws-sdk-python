"""Generated from Smithy shape ``com.amazonaws.networkmanager#DirectConnectGatewayAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment
    import capo_networkmanager.types.direct_connect_gateway_arn


class DirectConnectGatewayAttachment(TypedDict, closed=True):
    attachment: NotRequired["capo_networkmanager.types.attachment.Attachment"]
    direct_connect_gateway_arn: NotRequired[
        "capo_networkmanager.types.direct_connect_gateway_arn.DirectConnectGatewayArn"
    ]
    """<p>The Direct Connect gateway attachment ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DirectConnectGatewayAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_networkmanager.types.attachment

        out["Attachment"] = capo_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "direct_connect_gateway_arn" in value:
        out["DirectConnectGatewayArn"] = value["direct_connect_gateway_arn"]
    return out


def deserialize_json(data: dict) -> DirectConnectGatewayAttachment:
    out: DirectConnectGatewayAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import capo_networkmanager.types.attachment

        out["attachment"] = capo_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "DirectConnectGatewayArn" in data:
        out["direct_connect_gateway_arn"] = data["DirectConnectGatewayArn"]
    return out
