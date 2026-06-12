"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.sim_space_weaver_long_resource_name
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name
    import aws_sdk_simspaceweaver.types.simulation_app_status
    import aws_sdk_simspaceweaver.types.simulation_app_target_status


class SimulationAppMetadata(TypedDict):
    name: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_long_resource_name.SimSpaceWeaverLongResourceName"
    ]
    """<p>The name of the app.</p>"""
    simulation: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the simulation of the app.</p>"""
    domain: NotRequired[
        "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The domain of the app. For more information about domains, see <a href=\"https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains\">Key concepts: Domains</a> in the <i>SimSpace Weaver User Guide</i>.</p>"""
    status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_app_status.SimulationAppStatus"
    ]
    """<p>The current status of the app.</p>"""
    target_status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_app_target_status.SimulationAppTargetStatus"
    ]
    """<p>The desired status of the app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "simulation" in value:
        out["Simulation"] = value["simulation"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "status" in value:
        out["Status"] = value["status"]
    if "target_status" in value:
        out["TargetStatus"] = value["target_status"]
    return out


def deserialize_json(data: dict) -> SimulationAppMetadata:
    out: SimulationAppMetadata = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "TargetStatus" in data:
        out["target_status"] = data["TargetStatus"]
    return out
