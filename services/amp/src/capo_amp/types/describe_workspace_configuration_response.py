"""Generated from Smithy shape ``com.amazonaws.amp#DescribeWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.workspace_configuration_description


class DescribeWorkspaceConfigurationResponse(TypedDict, closed=True):
    workspace_configuration: "capo_amp.types.workspace_configuration_description.WorkspaceConfigurationDescription"
    """<p>This structure contains the information about the workspace configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.workspace_configuration_description

    out["workspaceConfiguration"] = (
        capo_amp.types.workspace_configuration_description.serialize_json(
            value["workspace_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationResponse:
    out: DescribeWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "workspaceConfiguration" in data:
        import capo_amp.types.workspace_configuration_description

        out["workspace_configuration"] = (
            capo_amp.types.workspace_configuration_description.deserialize_json(
                data["workspaceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWorkspaceConfigurationResponse.workspace_configuration required"
        )
    return out
