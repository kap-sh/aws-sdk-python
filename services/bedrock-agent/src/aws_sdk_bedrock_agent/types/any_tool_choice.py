"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AnyToolChoice``."""

from typing_extensions import TypedDict


class AnyToolChoice(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AnyToolChoice) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AnyToolChoice:
    out: AnyToolChoice = {}  # type: ignore[typeddict-item]
    return out
