"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartAppInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.client_token
    import aws_sdk_simspaceweaver.types.description
    import aws_sdk_simspaceweaver.types.launch_overrides
    import aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name


class StartAppInput(TypedDict):
    client_token: NotRequired["aws_sdk_simspaceweaver.types.client_token.ClientToken"]
    """<p>A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A <code>ClientToken</code> is also known as an <i>idempotency token</i>. A <code>ClientToken</code> expires after 24 hours.</p>"""
    simulation: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    name: "aws_sdk_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the app.</p>"""
    description: NotRequired["aws_sdk_simspaceweaver.types.description.Description"]
    """<p>The description of the app.</p>"""
    launch_overrides: NotRequired[
        "aws_sdk_simspaceweaver.types.launch_overrides.LaunchOverrides"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartAppInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Simulation"] = value["simulation"]
    out["Domain"] = value["domain"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "launch_overrides" in value:
        import aws_sdk_simspaceweaver.types.launch_overrides

        out["LaunchOverrides"] = (
            aws_sdk_simspaceweaver.types.launch_overrides.serialize_json(
                value["launch_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAppInput:
    out: StartAppInput = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Simulation" in data:
        out["simulation"] = data["Simulation"]
    else:
        raise DeserializationError("StartAppInput.simulation required")
    if "Domain" in data:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("StartAppInput.domain required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartAppInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "LaunchOverrides" in data:
        import aws_sdk_simspaceweaver.types.launch_overrides

        out["launch_overrides"] = (
            aws_sdk_simspaceweaver.types.launch_overrides.deserialize_json(
                data["LaunchOverrides"]
            )
        )
    return out
