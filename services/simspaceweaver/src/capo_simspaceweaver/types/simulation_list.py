"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simspaceweaver.types.simulation_metadata

SimulationList: TypeAlias = list[
    "capo_simspaceweaver.types.simulation_metadata.SimulationMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulationList) -> list:
    import capo_simspaceweaver.types.simulation_metadata

    out: list = []
    for item in value:
        out.append(capo_simspaceweaver.types.simulation_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> SimulationList:
    import capo_simspaceweaver.types.simulation_metadata

    out: SimulationList = []
    for item in data:
        out.append(capo_simspaceweaver.types.simulation_metadata.deserialize_json(item))
    return out
