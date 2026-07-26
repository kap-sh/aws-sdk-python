"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace

WorkspaceList: TypeAlias = list["capo_workspaces.types.workspace.Workspace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceList) -> list:
    import capo_workspaces.types.workspace

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceList:
    import capo_workspaces.types.workspace

    out: WorkspaceList = []
    for item in data:
        out.append(capo_workspaces.types.workspace.deserialize_aws_json_1_1(item))
    return out
