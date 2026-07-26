"""Generated from Smithy shape ``com.amazonaws.deadline#PriorityFifoSchedulingConfiguration``."""

from typing_extensions import TypedDict


class PriorityFifoSchedulingConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PriorityFifoSchedulingConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PriorityFifoSchedulingConfiguration:
    out: PriorityFifoSchedulingConfiguration = {}  # type: ignore[typeddict-item]
    return out
