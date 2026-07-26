"""Generated from Smithy shape ``com.amazonaws.socialmessaging#PostWhatsAppMessageMediaOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_media_id


class PostWhatsAppMessageMediaOutput(TypedDict, closed=True):
    media_id: NotRequired[
        "capo_socialmessaging.types.whats_app_media_id.WhatsAppMediaId"
    ]
    """<p>The unique identifier of the posted WhatsApp message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostWhatsAppMessageMediaOutput) -> dict:
    out: dict = {}
    if "media_id" in value:
        out["mediaId"] = value["media_id"]
    return out


def deserialize_json(data: dict) -> PostWhatsAppMessageMediaOutput:
    out: PostWhatsAppMessageMediaOutput = {}  # type: ignore[typeddict-item]
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    return out
