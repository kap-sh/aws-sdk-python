"""Generated from Smithy shape ``com.amazonaws.workspaces#ModifyWorkspacePropertiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.data_replication
    import aws_sdk_workspaces.types.workspace_id
    import aws_sdk_workspaces.types.workspace_properties


class ModifyWorkspacePropertiesRequest(TypedDict):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    workspace_properties: NotRequired[
        "aws_sdk_workspaces.types.workspace_properties.WorkspaceProperties"
    ]
    """<p>The properties of the WorkSpace.</p>"""
    data_replication: NotRequired[
        "aws_sdk_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates the data replication status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyWorkspacePropertiesRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    if "workspace_properties" in value:
        import aws_sdk_workspaces.types.workspace_properties

        out["WorkspaceProperties"] = (
            aws_sdk_workspaces.types.workspace_properties.serialize_aws_json_1_1(
                value["workspace_properties"]
            )
        )
    if "data_replication" in value:
        import aws_sdk_workspaces.types.data_replication

        out["DataReplication"] = (
            aws_sdk_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyWorkspacePropertiesRequest:
    out: ModifyWorkspacePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError(
            "ModifyWorkspacePropertiesRequest.workspace_id required"
        )
    if "WorkspaceProperties" in data:
        import aws_sdk_workspaces.types.workspace_properties

        out["workspace_properties"] = (
            aws_sdk_workspaces.types.workspace_properties.deserialize_aws_json_1_1(
                data["WorkspaceProperties"]
            )
        )
    if "DataReplication" in data:
        import aws_sdk_workspaces.types.data_replication

        out["data_replication"] = (
            aws_sdk_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    return out
