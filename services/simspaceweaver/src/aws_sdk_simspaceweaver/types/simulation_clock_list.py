"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationClockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.simulation_clock

SimulationClockList: TypeAlias = list[
    "aws_sdk_simspaceweaver.types.simulation_clock.SimulationClock"
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulationClockList) -> list:
    import aws_sdk_simspaceweaver.types.simulation_clock

    out: list = []
    for item in value:
        out.append(aws_sdk_simspaceweaver.types.simulation_clock.serialize_json(item))
    return out


def deserialize_json(data: list) -> SimulationClockList:
    import aws_sdk_simspaceweaver.types.simulation_clock

    out: SimulationClockList = []
    for item in data:
        out.append(aws_sdk_simspaceweaver.types.simulation_clock.deserialize_json(item))
    return out
