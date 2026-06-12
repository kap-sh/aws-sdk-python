"""Generated from Smithy shape ``com.amazonaws.networkmanager#AcceptAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id


class AcceptAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AcceptAttachmentRequest:
    out: AcceptAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
