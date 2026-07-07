"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectAttachmentOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.tunnel_protocol


class ConnectAttachmentOptions(TypedDict, closed=True):
    protocol: NotRequired["aws_sdk_networkmanager.types.tunnel_protocol.TunnelProtocol"]
    """<p>The protocol used for the attachment connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAttachmentOptions) -> dict:
    out: dict = {}
    if "protocol" in value:
        import aws_sdk_networkmanager.types.tunnel_protocol

        out["Protocol"] = aws_sdk_networkmanager.types.tunnel_protocol.serialize_json(
            value["protocol"]
        )
    return out


def deserialize_json(data: dict) -> ConnectAttachmentOptions:
    out: ConnectAttachmentOptions = {}  # type: ignore[typeddict-item]
    if "Protocol" in data:
        import aws_sdk_networkmanager.types.tunnel_protocol

        out["protocol"] = aws_sdk_networkmanager.types.tunnel_protocol.deserialize_json(
            data["Protocol"]
        )
    return out
