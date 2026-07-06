"""Generated from Smithy shape ``com.amazonaws.chime#RedactRoomMessageResponse``."""

from typing_extensions import TypedDict


class RedactRoomMessageResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RedactRoomMessageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RedactRoomMessageResponse:
    out: RedactRoomMessageResponse = {}  # type: ignore[typeddict-item]
    return out
