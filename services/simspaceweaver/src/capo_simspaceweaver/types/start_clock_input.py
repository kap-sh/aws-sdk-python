"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartClockInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class StartClockInput(TypedDict, closed=True):
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartClockInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    return out


def deserialize_json(data: dict) -> StartClockInput:
    out: StartClockInput = {}  # type: ignore[typeddict-item]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    else:
        raise DeserializationError("StartClockInput.simulation required")
    return out
