"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.workspace_id
    import aws_sdk_workspaces.types.workspace_image_description
    import aws_sdk_workspaces.types.workspace_image_name


class CreateWorkspaceImageRequest(TypedDict, closed=True):
    name: "aws_sdk_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the new WorkSpace image.</p>"""
    description: (
        "aws_sdk_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>The description of the new WorkSpace image.</p>"""
    workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the source WorkSpace</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags that you want to add to the new WorkSpace image. To add tags when you're creating the image, you must create an IAM policy that grants your IAM user permission to use <code>workspaces:CreateTags</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["WorkspaceId"] = value["workspace_id"]
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceImageRequest:
    out: CreateWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateWorkspaceImageRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateWorkspaceImageRequest.description required")
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        raise DeserializationError("CreateWorkspaceImageRequest.workspace_id required")
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
