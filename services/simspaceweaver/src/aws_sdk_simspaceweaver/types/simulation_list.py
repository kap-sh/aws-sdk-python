"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.simulation_metadata

SimulationList: TypeAlias = list[
    "aws_sdk_simspaceweaver.types.simulation_metadata.SimulationMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: SimulationList) -> list:
    import aws_sdk_simspaceweaver.types.simulation_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SimulationList:
    import aws_sdk_simspaceweaver.types.simulation_metadata

    out: SimulationList = []
    for item in data:
        out.append(
            aws_sdk_simspaceweaver.types.simulation_metadata.deserialize_json(item)
        )
    return out
