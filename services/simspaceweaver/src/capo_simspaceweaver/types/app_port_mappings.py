"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#AppPortMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_simspaceweaver.types.simulation_app_port_mapping

AppPortMappings: TypeAlias = list[
    "capo_simspaceweaver.types.simulation_app_port_mapping.SimulationAppPortMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppPortMappings) -> list:
    import capo_simspaceweaver.types.simulation_app_port_mapping

    out: list = []
    for item in value:
        out.append(
            capo_simspaceweaver.types.simulation_app_port_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AppPortMappings:
    import capo_simspaceweaver.types.simulation_app_port_mapping

    out: AppPortMappings = []
    for item in data:
        out.append(
            capo_simspaceweaver.types.simulation_app_port_mapping.deserialize_json(item)
        )
    return out
