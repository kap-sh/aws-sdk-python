"""Generated from Smithy shape ``com.amazonaws.qbusiness#EndOfInputEvent``."""

from typing import TypedDict


class EndOfInputEvent(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EndOfInputEvent) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EndOfInputEvent:
    out: EndOfInputEvent = {}  # type: ignore[typeddict-item]
    return out
