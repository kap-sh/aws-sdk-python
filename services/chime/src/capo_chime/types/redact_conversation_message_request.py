"""Generated from Smithy shape ``com.amazonaws.chime#RedactConversationMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string


class RedactConversationMessageRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    conversation_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The conversation ID.</p>"""
    message_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The message ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactConversationMessageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RedactConversationMessageRequest:
    out: RedactConversationMessageRequest = {}  # type: ignore[typeddict-item]
    return out
