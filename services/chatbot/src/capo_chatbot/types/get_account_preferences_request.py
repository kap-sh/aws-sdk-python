"""Generated from Smithy shape ``com.amazonaws.chatbot#GetAccountPreferencesRequest``."""

from typing_extensions import TypedDict


class GetAccountPreferencesRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountPreferencesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountPreferencesRequest:
    out: GetAccountPreferencesRequest = {}  # type: ignore[typeddict-item]
    return out
