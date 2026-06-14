"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateUpdatedWorkspaceImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.workspace_image_description
    import aws_sdk_workspaces.types.workspace_image_id
    import aws_sdk_workspaces.types.workspace_image_name


class CreateUpdatedWorkspaceImageRequest(TypedDict):
    name: "aws_sdk_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the new updated WorkSpace image.</p>"""
    description: (
        "aws_sdk_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>A description of whether updates for the WorkSpace image are available.</p>"""
    source_image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the source WorkSpace image.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags that you want to add to the new updated WorkSpace image.</p> <note> <p>To add tags at the same time when you're creating the updated image, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Description"] = value["description"]
    out["SourceImageId"] = value["source_image_id"]
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedWorkspaceImageRequest:
    out: CreateUpdatedWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateUpdatedWorkspaceImageRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError(
            "CreateUpdatedWorkspaceImageRequest.description required"
        )
    if "SourceImageId" in data:
        out["source_image_id"] = data["SourceImageId"]
    else:
        raise DeserializationError(
            "CreateUpdatedWorkspaceImageRequest.source_image_id required"
        )
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
