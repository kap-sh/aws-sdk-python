"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.tag_key_list
    import aws_sdk_workspaces_instances.types.workspace_instance_id


class UntagResourceRequest(TypedDict):
    workspace_instance_id: (
        "aws_sdk_workspaces_instances.types.workspace_instance_id.WorkspaceInstanceId"
    )
    """<p>Unique identifier of the WorkSpace Instance to untag.</p>"""
    tag_keys: "aws_sdk_workspaces_instances.types.tag_key_list.TagKeyList"
    """<p>Keys of tags to be removed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["WorkspaceInstanceId"] = value["workspace_instance_id"]
    import aws_sdk_workspaces_instances.types.tag_key_list

    out["TagKeys"] = (
        aws_sdk_workspaces_instances.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "WorkspaceInstanceId" in data:
        out["workspace_instance_id"] = data["WorkspaceInstanceId"]
    else:
        raise DeserializationError(
            "UntagResourceRequest.workspace_instance_id required"
        )
    if "TagKeys" in data:
        import aws_sdk_workspaces_instances.types.tag_key_list

        out["tag_keys"] = (
            aws_sdk_workspaces_instances.types.tag_key_list.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
