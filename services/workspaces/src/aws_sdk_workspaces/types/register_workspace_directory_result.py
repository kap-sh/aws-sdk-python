"""Generated from Smithy shape ``com.amazonaws.workspaces#RegisterWorkspaceDirectoryResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.workspace_directory_state


class RegisterWorkspaceDirectoryResult(TypedDict):
    directory_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.workspace_directory_state.WorkspaceDirectoryState"
    ]
    """<p>The registration status of the WorkSpace directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWorkspaceDirectoryResult) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "state" in value:
        import aws_sdk_workspaces.types.workspace_directory_state

        out["State"] = (
            aws_sdk_workspaces.types.workspace_directory_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWorkspaceDirectoryResult:
    out: RegisterWorkspaceDirectoryResult = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "State" in data:
        import aws_sdk_workspaces.types.workspace_directory_state

        out["state"] = (
            aws_sdk_workspaces.types.workspace_directory_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
