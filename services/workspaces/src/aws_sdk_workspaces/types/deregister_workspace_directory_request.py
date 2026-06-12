"""Generated from Smithy shape ``com.amazonaws.workspaces#DeregisterWorkspaceDirectoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.directory_id


class DeregisterWorkspaceDirectoryRequest(TypedDict):
    directory_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The identifier of the directory. If any WorkSpaces are registered to this directory, you must remove them before you deregister the directory, or you will receive an OperationNotSupportedException error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterWorkspaceDirectoryRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterWorkspaceDirectoryRequest:
    out: DeregisterWorkspaceDirectoryRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "DeregisterWorkspaceDirectoryRequest.directory_id required"
        )
    return out
