"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id


class GetVpcAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVpcAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVpcAttachmentRequest:
    out: GetVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
