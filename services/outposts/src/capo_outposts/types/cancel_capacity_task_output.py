"""Generated from Smithy shape ``com.amazonaws.outposts#CancelCapacityTaskOutput``."""

from typing_extensions import TypedDict


class CancelCapacityTaskOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelCapacityTaskOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelCapacityTaskOutput:
    out: CancelCapacityTaskOutput = {}  # type: ignore[typeddict-item]
    return out
