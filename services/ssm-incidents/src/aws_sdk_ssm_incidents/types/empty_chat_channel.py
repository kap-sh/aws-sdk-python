"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EmptyChatChannel``."""

from typing import TypedDict


class EmptyChatChannel(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EmptyChatChannel) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EmptyChatChannel:
    out: EmptyChatChannel = {}  # type: ignore[typeddict-item]
    return out
