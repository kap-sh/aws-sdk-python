"""Generated from Smithy shape ``com.amazonaws.workspaces#DirectoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_directory

DirectoryList: TypeAlias = list[
    "capo_workspaces.types.workspace_directory.WorkspaceDirectory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DirectoryList) -> list:
    import capo_workspaces.types.workspace_directory

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.workspace_directory.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DirectoryList:
    import capo_workspaces.types.workspace_directory

    out: DirectoryList = []
    for item in data:
        out.append(
            capo_workspaces.types.workspace_directory.deserialize_aws_json_1_1(item)
        )
    return out
