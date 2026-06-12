"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.connect_attachment_options


class ConnectAttachment(TypedDict):
    attachment: NotRequired["aws_sdk_networkmanager.types.attachment.Attachment"]
    """<p>The attachment details.</p>"""
    transport_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the transport attachment.</p>"""
    options: NotRequired[
        "aws_sdk_networkmanager.types.connect_attachment_options.ConnectAttachmentOptions"
    ]
    """<p>Options for connecting an attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_networkmanager.types.attachment

        out["Attachment"] = aws_sdk_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "transport_attachment_id" in value:
        out["TransportAttachmentId"] = value["transport_attachment_id"]
    if "options" in value:
        import aws_sdk_networkmanager.types.connect_attachment_options

        out["Options"] = (
            aws_sdk_networkmanager.types.connect_attachment_options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectAttachment:
    out: ConnectAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_networkmanager.types.attachment

        out["attachment"] = aws_sdk_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "TransportAttachmentId" in data:
        out["transport_attachment_id"] = data["TransportAttachmentId"]
    if "Options" in data:
        import aws_sdk_networkmanager.types.connect_attachment_options

        out["options"] = (
            aws_sdk_networkmanager.types.connect_attachment_options.deserialize_json(
                data["Options"]
            )
        )
    return out
