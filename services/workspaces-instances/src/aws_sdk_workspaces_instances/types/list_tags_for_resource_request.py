"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class ListTagsForResourceRequest(TypedDict, closed=True):
    workspace_instance_id: (
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError(
            "ListTagsForResourceRequest.workspace_instance_id required"
        )
    return out
