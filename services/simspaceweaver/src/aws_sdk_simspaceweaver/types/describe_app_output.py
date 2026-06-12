"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#DescribeAppOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.description
    import aws_sdk_simspaceweaver.types.launch_overrides
    import aws_sdk_simspaceweaver.types.sim_space_weaver_long_resource_name
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name
    import aws_sdk_simspaceweaver.types.simulation_app_endpoint_info
    import aws_sdk_simspaceweaver.types.simulation_app_status
    import aws_sdk_simspaceweaver.types.simulation_app_target_status


class DescribeAppOutput(TypedDict):
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
    """<p>The name of the domain of the app.</p>"""
    status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_app_status.SimulationAppStatus"
    ]
    """<p>The current lifecycle state of the custom app.</p>"""
    target_status: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_app_target_status.SimulationAppTargetStatus"
    ]
    """<p>The desired lifecycle state of the custom app.</p>"""
    launch_overrides: NotRequired[
        "aws_sdk_simspaceweaver.types.launch_overrides.LaunchOverrides"
    ]
    description: NotRequired["aws_sdk_simspaceweaver.types.description.Description"]
    """<p>The description of the app.</p>"""
    endpoint_info: NotRequired[
        "aws_sdk_simspaceweaver.types.simulation_app_endpoint_info.SimulationAppEndpointInfo"
    ]
    """<p>Information about the network endpoint for the custom app. You can use the endpoint to connect to the custom app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppOutput) -> dict:
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
    if "launch_overrides" in value:
        import aws_sdk_simspaceweaver.types.launch_overrides

        out["LaunchOverrides"] = (
            aws_sdk_simspaceweaver.types.launch_overrides.serialize_json(
                value["launch_overrides"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "endpoint_info" in value:
        import aws_sdk_simspaceweaver.types.simulation_app_endpoint_info

        out["EndpointInfo"] = (
            aws_sdk_simspaceweaver.types.simulation_app_endpoint_info.serialize_json(
                value["endpoint_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppOutput:
    out: DescribeAppOutput = {}  # type: ignore[typeddict-item]
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
    if "LaunchOverrides" in data:
        import aws_sdk_simspaceweaver.types.launch_overrides

        out["launch_overrides"] = (
            aws_sdk_simspaceweaver.types.launch_overrides.deserialize_json(
                data["LaunchOverrides"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndpointInfo" in data:
        import aws_sdk_simspaceweaver.types.simulation_app_endpoint_info

        out["endpoint_info"] = (
            aws_sdk_simspaceweaver.types.simulation_app_endpoint_info.deserialize_json(
                data["EndpointInfo"]
            )
        )
    return out
