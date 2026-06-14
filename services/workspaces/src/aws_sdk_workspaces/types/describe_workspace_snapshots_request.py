"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_id


class DescribeWorkspaceSnapshotsRequest(TypedDict):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceSnapshotsRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceSnapshotsRequest:
    out: DescribeWorkspaceSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError(
            "DescribeWorkspaceSnapshotsRequest.workspace_id required"
        )
    return out
