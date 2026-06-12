"""Generated from Smithy shape ``com.amazonaws.connectcases#EmptyFieldValue``."""

from typing import TypedDict


class EmptyFieldValue(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EmptyFieldValue) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EmptyFieldValue:
    out: EmptyFieldValue = {}  # type: ignore[typeddict-item]
    return out
