"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#AppPortMappings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.simulation_app_port_mapping

AppPortMappings: TypeAlias = list[
    "aws_sdk_simspaceweaver.types.simulation_app_port_mapping.SimulationAppPortMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppPortMappings) -> list:
    import aws_sdk_simspaceweaver.types.simulation_app_port_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_app_port_mapping.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppPortMappings:
    import aws_sdk_simspaceweaver.types.simulation_app_port_mapping

    out: AppPortMappings = []
    for item in data:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_app_port_mapping.deserialize_json(
                item
            )
        )
    return out
