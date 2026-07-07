"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment


class DeleteAttachmentResponse(TypedDict, closed=True):
    attachment: NotRequired["aws_sdk_networkmanager.types.attachment.Attachment"]
    """<p>Information about the deleted attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_networkmanager.types.attachment

        out["Attachment"] = aws_sdk_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    return out


def deserialize_json(data: dict) -> DeleteAttachmentResponse:
    out: DeleteAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_networkmanager.types.attachment

        out["attachment"] = aws_sdk_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    return out
