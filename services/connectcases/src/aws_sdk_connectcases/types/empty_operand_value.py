"""Generated from Smithy shape ``com.amazonaws.connectcases#EmptyOperandValue``."""

from typing import TypedDict


class EmptyOperandValue(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EmptyOperandValue) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EmptyOperandValue:
    out: EmptyOperandValue = {}  # type: ignore[typeddict-item]
    return out
