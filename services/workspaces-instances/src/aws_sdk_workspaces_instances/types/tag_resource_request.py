"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.tag_list
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class TagResourceRequest(TypedDict):
    workspace_instance_id: (
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance to tag.</p>"""
    tags: "aws_sdk_workspaces_instances.types.tag_list.TagList"
    """<p>Tags to be added to the WorkSpace Instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    import aws_sdk_workspaces_instances.types.tag_list

    out["Tags"] = aws_sdk_workspaces_instances.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError("TagResourceRequest.workspace_instance_id required")
    if "Tags" in data:
        import aws_sdk_workspaces_instances.types.tag_list

        out["tags"] = (
            aws_sdk_workspaces_instances.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
