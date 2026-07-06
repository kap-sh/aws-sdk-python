"""Generated from Smithy shape ``com.amazonaws.outposts#CancelOrderOutput``."""

from typing_extensions import TypedDict


class CancelOrderOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelOrderOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelOrderOutput:
    out: CancelOrderOutput = {}  # type: ignore[typeddict-item]
    return out
