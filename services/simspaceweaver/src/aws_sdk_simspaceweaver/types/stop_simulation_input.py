"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopSimulationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class StopSimulationInput(TypedDict):
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopSimulationInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    return out


def deserialize_json(data: dict) -> StopSimulationInput:
    out: StopSimulationInput = {}  # type: ignore[typeddict-item]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    else:
        raise DeserializationError("StopSimulationInput.simulation required")
    return out
