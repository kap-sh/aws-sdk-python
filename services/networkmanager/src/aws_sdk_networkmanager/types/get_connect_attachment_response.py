"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_attachment


class GetConnectAttachmentResponse(TypedDict, closed=True):
    connect_attachment: NotRequired[
        "aws_sdk_networkmanager.types.connect_attachment.ConnectAttachment"
    ]
    """<p>Details about the Connect attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectAttachmentResponse) -> dict:
    out: dict = {}
    if "connect_attachment" in value:
        import aws_sdk_networkmanager.types.connect_attachment

        out["ConnectAttachment"] = (
            aws_sdk_networkmanager.types.connect_attachment.serialize_json(
                value["connect_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectAttachmentResponse:
    out: GetConnectAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "ConnectAttachment" in data:
        import aws_sdk_networkmanager.types.connect_attachment

        out["connect_attachment"] = (
            aws_sdk_networkmanager.types.connect_attachment.deserialize_json(
                data["ConnectAttachment"]
            )
        )
    return out
