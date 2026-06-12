"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StopAppInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class StopAppInput(TypedDict):
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    app: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopAppInput) -> dict:
    out: dict = {}
    out["Simulation"] = value["simulation"]
    out["Domain"] = value["domain"]
    out["App"] = value["app"]
    return out


def deserialize_json(data: dict) -> StopAppInput:
    out: StopAppInput = {}  # type: ignore[typeddict-item]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    else:
        raise DeserializationError("StopAppInput.simulation required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("StopAppInput.domain required")
    if "App" in data:
        out["app"] = data["App"]
    else:
        raise DeserializationError("StopAppInput.app required")
    return out
