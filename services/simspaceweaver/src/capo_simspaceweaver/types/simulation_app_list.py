"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simspaceweaver.types.simulation_app_metadata

SimulationAppList: TypeAlias = list[
    "capo_simspaceweaver.types.simulation_app_metadata.SimulationAppMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppList) -> list:
    import capo_simspaceweaver.types.simulation_app_metadata

    out: list = []
    for item in value:
        out.append(
            capo_simspaceweaver.types.simulation_app_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SimulationAppList:
    import capo_simspaceweaver.types.simulation_app_metadata

    out: SimulationAppList = []
    for item in data:
        out.append(
            capo_simspaceweaver.types.simulation_app_metadata.deserialize_json(item)
        )
    return out
