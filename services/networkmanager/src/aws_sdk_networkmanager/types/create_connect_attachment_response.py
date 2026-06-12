"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectAttachmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_attachment


class CreateConnectAttachmentResponse(TypedDict):
    connect_attachment: NotRequired[
        "aws_sdk_networkmanager.types.connect_attachment.ConnectAttachment"
    ]
    """<p>The response to a Connect attachment request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectAttachmentResponse) -> dict:
    out: dict = {}
    if "connect_attachment" in value:
        import aws_sdk_networkmanager.types.connect_attachment

        out["ConnectAttachment"] = (
            aws_sdk_networkmanager.types.connect_attachment.serialize_json(
                value["connect_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateConnectAttachmentResponse:
    out: CreateConnectAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "ConnectAttachment" in data:
        import aws_sdk_networkmanager.types.connect_attachment

        out["connect_attachment"] = (
            aws_sdk_networkmanager.types.connect_attachment.deserialize_json(
                data["ConnectAttachment"]
            )
        )
    return out
