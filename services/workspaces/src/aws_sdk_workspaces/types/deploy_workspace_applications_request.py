"""Generated from Smithy shape ``com.amazonaws.workspaces#DeployWorkspaceApplicationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.boolean_object
    import aws_sdk_workspaces.types.workspace_id


class DeployWorkspaceApplicationsRequest(TypedDict):
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    force: NotRequired["aws_sdk_workspaces.types.boolean_object.BooleanObject"]
    """<p>Indicates whether the force flag is applied for the specified WorkSpace. When the force flag is enabled, it allows previously failed deployments to be retried.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployWorkspaceApplicationsRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    if "force" in value:
        out["Force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployWorkspaceApplicationsRequest:
    out: DeployWorkspaceApplicationsRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError(
            "DeployWorkspaceApplicationsRequest.workspace_id required"
        )
    if "Force" in data:
        out["force"] = data["Force"]
    return out
