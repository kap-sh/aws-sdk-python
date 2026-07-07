"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetSiteToSiteVpnAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id


class GetSiteToSiteVpnAttachmentRequest(TypedDict, closed=True):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSiteToSiteVpnAttachmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSiteToSiteVpnAttachmentRequest:
    out: GetSiteToSiteVpnAttachmentRequest = {}  # type: ignore[typeddict-item]
    return out
