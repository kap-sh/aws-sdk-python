"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AutoToolChoice``."""

from typing_extensions import TypedDict


class AutoToolChoice(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AutoToolChoice) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AutoToolChoice:
    out: AutoToolChoice = {}  # type: ignore[typeddict-item]
    return out
