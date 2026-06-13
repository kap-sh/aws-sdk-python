"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListWorkspaceInstancesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.next_token
    import aws_sdk_workspaces_instances.types.workspace_instances


class ListWorkspaceInstancesResponse(TypedDict):
    workspace_instances: (
        "aws_sdk_workspaces_instances.types.workspace_instances.WorkspaceInstances"
    )
    """<p>Collection of WorkSpaces Instances returned by the query.</p>"""
    next_token: NotRequired["aws_sdk_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional WorkSpaces Instances if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkspaceInstancesResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_instances.types.workspace_instances

    out["WorkspaceInstances"] = (
        aws_sdk_workspaces_instances.types.workspace_instances.serialize_aws_json_1_0(
            value["workspace_instances"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkspaceInstancesResponse:
    out: ListWorkspaceInstancesResponse = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstances" in data:
        import aws_sdk_workspaces_instances.types.workspace_instances

        out["workspace_instances"] = (
            aws_sdk_workspaces_instances.types.workspace_instances.deserialize_aws_json_1_0(
                data["WorkspaceInstances"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkspaceInstancesResponse.workspace_instances required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
