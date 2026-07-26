"""Generated from Smithy shape ``com.amazonaws.networkmanager#AcceptAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment


class AcceptAttachmentResponse(TypedDict, closed=True):
    attachment: NotRequired["capo_networkmanager.types.attachment.Attachment"]
    """<p>The response to the attachment request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_networkmanager.types.attachment

        out["Attachment"] = capo_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    return out


def deserialize_json(data: dict) -> AcceptAttachmentResponse:
    out: AcceptAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import capo_networkmanager.types.attachment

        out["attachment"] = capo_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    return out
