"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.simulation_app_metadata

SimulationAppList: TypeAlias = list[
    "aws_sdk_simspaceweaver.types.simulation_app_metadata.SimulationAppMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppList) -> list:
    import aws_sdk_simspaceweaver.types.simulation_app_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_app_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SimulationAppList:
    import aws_sdk_simspaceweaver.types.simulation_app_metadata

    out: SimulationAppList = []
    for item in data:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_app_metadata.deserialize_json(item)
        )
    return out
