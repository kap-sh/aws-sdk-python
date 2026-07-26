"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetMediaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.media_id
    import capo_qbusiness.types.message_id


class GetMediaRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business which contains the media object.</p>"""
    conversation_id: "capo_qbusiness.types.conversation_id.ConversationId"
    """<p>The identifier of the Amazon Q Business conversation.</p>"""
    message_id: "capo_qbusiness.types.message_id.MessageId"
    """<p>The identifier of the Amazon Q Business message.</p>"""
    media_id: "capo_qbusiness.types.media_id.MediaId"
    """<p>The identifier of the media object. You can find this in the <code>sourceAttributions</code> returned by the <code>Chat</code>, <code>ChatSync</code>, and <code>ListMessages</code> API responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMediaRequest:
    out: GetMediaRequest = {}  # type: ignore[typeddict-item]
    return out
