"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopAppOutput``."""

from typing_extensions import TypedDict


class StopAppOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopAppOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopAppOutput:
    out: StopAppOutput = {}  # type: ignore[typeddict-item]
    return out
