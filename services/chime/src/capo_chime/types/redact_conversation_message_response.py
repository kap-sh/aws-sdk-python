"""Generated from Smithy shape ``com.amazonaws.chime#RedactConversationMessageResponse``."""

from typing_extensions import TypedDict


class RedactConversationMessageResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RedactConversationMessageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RedactConversationMessageResponse:
    out: RedactConversationMessageResponse = {}  # type: ignore[typeddict-item]
    return out
