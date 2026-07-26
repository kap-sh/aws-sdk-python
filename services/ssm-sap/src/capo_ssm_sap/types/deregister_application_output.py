"""Generated from Smithy shape ``com.amazonaws.ssmsap#DeregisterApplicationOutput``."""

from typing_extensions import TypedDict


class DeregisterApplicationOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterApplicationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterApplicationOutput:
    out: DeregisterApplicationOutput = {}  # type: ignore[typeddict-item]
    return out
