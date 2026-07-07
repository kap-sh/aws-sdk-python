"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#TagStreamOutput``."""

from typing_extensions import TypedDict


class TagStreamOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: TagStreamOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> TagStreamOutput:
    out: TagStreamOutput = {}  # type: ignore[typeddict-item]
    return out
