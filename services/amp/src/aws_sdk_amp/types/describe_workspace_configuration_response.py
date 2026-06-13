"""Generated from Smithy shape ``com.amazonaws.amp#DescribeWorkspaceConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_configuration_description


class DescribeWorkspaceConfigurationResponse(TypedDict):
    workspace_configuration: "aws_sdk_amp.types.workspace_configuration_description.WorkspaceConfigurationDescription"
    """<p>This structure contains the information about the workspace configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.workspace_configuration_description

    out["workspaceConfiguration"] = (
        aws_sdk_amp.types.workspace_configuration_description.serialize_json(
            value["workspace_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationResponse:
    out: DescribeWorkspaceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "workspaceConfiguration" in data:
        import aws_sdk_amp.types.workspace_configuration_description

        out["workspace_configuration"] = (
            aws_sdk_amp.types.workspace_configuration_description.deserialize_json(
                data["workspaceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWorkspaceConfigurationResponse.workspace_configuration required"
        )
    return out
