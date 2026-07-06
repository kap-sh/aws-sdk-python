"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopSimulationOutput``."""

from typing_extensions import TypedDict


class StopSimulationOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopSimulationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSimulationOutput:
    out: StopSimulationOutput = {}  # type: ignore[typeddict-item]
    return out
