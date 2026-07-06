"""Generated from Smithy shape ``com.amazonaws.connectcases#EmptyFieldValue``."""

from typing_extensions import TypedDict


class EmptyFieldValue(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EmptyFieldValue) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EmptyFieldValue:
    out: EmptyFieldValue = {}  # type: ignore[typeddict-item]
    return out
