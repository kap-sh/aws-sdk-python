"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspaceAccessPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.workspace_access_properties


class ModifyWorkspaceAccessPropertiesRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory.</p>"""
    workspace_access_properties: (
        "capo_workspaces.types.workspace_access_properties.WorkspaceAccessProperties"
    )
    """<p>The device types and operating systems to enable or disable for access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspaceAccessPropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.workspace_access_properties

    out["WorkspaceAccessProperties"] = (
        capo_workspaces.types.workspace_access_properties.serialize_aws_json_1_1(
            value["workspace_access_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspaceAccessPropertiesRequest:
    out: ModifyWorkspaceAccessPropertiesRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "ModifyWorkspaceAccessPropertiesRequest.resource_id required"
        )
    if "WorkspaceAccessProperties" in data:
        import capo_workspaces.types.workspace_access_properties

        out["workspace_access_properties"] = (
            capo_workspaces.types.workspace_access_properties.deserialize_aws_json_1_1(
                data["WorkspaceAccessProperties"]
            )
        )
    else:
        raise DeserializationError(
            "ModifyWorkspaceAccessPropertiesRequest.workspace_access_properties required"
        )
    return out
