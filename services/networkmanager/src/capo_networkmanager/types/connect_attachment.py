"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.connect_attachment_options


class ConnectAttachment(TypedDict, closed=True):
    attachment: NotRequired["capo_networkmanager.types.attachment.Attachment"]
    """<p>The attachment details.</p>"""
    transport_attachment_id: NotRequired[
        "capo_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of the transport attachment.</p>"""
    options: NotRequired[
        "capo_networkmanager.types.connect_attachment_options.ConnectAttachmentOptions"
    ]
    """<p>Options for connecting an attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_networkmanager.types.attachment

        out["Attachment"] = capo_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "transport_attachment_id" in value:
        out["TransportAttachmentId"] = value["transport_attachment_id"]
    if "options" in value:
        import capo_networkmanager.types.connect_attachment_options

        out["Options"] = (
            capo_networkmanager.types.connect_attachment_options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectAttachment:
    out: ConnectAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import capo_networkmanager.types.attachment

        out["attachment"] = capo_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "TransportAttachmentId" in data:
        out["transport_attachment_id"] = data["TransportAttachmentId"]
    if "Options" in data:
        import capo_networkmanager.types.connect_attachment_options

        out["options"] = (
            capo_networkmanager.types.connect_attachment_options.deserialize_json(
                data["Options"]
            )
        )
    return out
