"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceCreationPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.workspace_creation_properties


class ModifyWorkspaceCreationPropertiesRequest(TypedDict, closed=True):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    workspace_creation_properties: "aws_sdk_workspaces.types.workspace_creation_properties.WorkspaceCreationProperties"
    """<p>The default properties for creating WorkSpaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceCreationPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_workspaces.types.workspace_creation_properties

    out["WorkspaceCreationProperties"] = (
        aws_sdk_workspaces.types.workspace_creation_properties.serialize_aws_json_1_1(
            value["workspace_creation_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceCreationPropertiesRequest:
    out: ModifyWorkspaceCreationPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "ModifyWorkspaceCreationPropertiesRequest.resource_id required"
        )
    if "WorkspaceCreationProperties" in data:
        import aws_sdk_workspaces.types.workspace_creation_properties

        out["workspace_creation_properties"] = (
            aws_sdk_workspaces.types.workspace_creation_properties.deserialize_aws_json_1_1(
                data["WorkspaceCreationProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyWorkspaceCreationPropertiesRequest.workspace_creation_properties required"
        )
    return out
