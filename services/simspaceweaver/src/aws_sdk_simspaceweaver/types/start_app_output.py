"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartAppOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class StartAppOutput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the app.</p>"""
    domain: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the domain of the app.</p>"""
    simulation: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAppOutput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "simulation" in value:
        out["Simulation"] = value["simulation"]
    return out


def deserialize_json(data: dict) -> StartAppOutput:
    out: StartAppOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    return out
