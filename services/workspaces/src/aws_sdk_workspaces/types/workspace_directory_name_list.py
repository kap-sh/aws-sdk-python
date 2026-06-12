"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_directory_name

WorkspaceDirectoryNameList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceDirectoryNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspaceDirectoryNameList:
    return list(data)
