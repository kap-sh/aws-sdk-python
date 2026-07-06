"""Generated from Smithy shape ``com.amazonaws.workspaces#CopyWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.region
    import aws_sdk_workspaces.types.tag_list
    import aws_sdk_workspaces.types.workspace_image_description
    import aws_sdk_workspaces.types.workspace_image_id
    import aws_sdk_workspaces.types.workspace_image_name


class CopyWorkspaceImageRequest(TypedDict, closed=True):
    name: "aws_sdk_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the image.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    ]
    """<p>A description of the image.</p>"""
    source_image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the source image.</p>"""
    source_region: "aws_sdk_workspaces.types.region.Region"
    """<p>The identifier of the source Region.</p>"""
    tags: NotRequired["aws_sdk_workspaces.types.tag_list.TagList"]
    """<p>The tags for the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["SourceImageId"] = value["source_image_id"]
    out["SourceRegion"] = value["source_region"]
    if "tags" in value:
        import aws_sdk_workspaces.types.tag_list

        out["Tags"] = aws_sdk_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyWorkspaceImageRequest:
    out: CopyWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CopyWorkspaceImageRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "SourceImageId" in data:
        out["source_image_id"] = data["SourceImageId"]
    else:
        raise DeserializationError("CopyWorkspaceImageRequest.source_image_id required")
    if "SourceRegion" in data:
        out["source_region"] = data["SourceRegion"]
    else:
        raise DeserializationError("CopyWorkspaceImageRequest.source_region required")
    if "Tags" in data:
        import aws_sdk_workspaces.types.tag_list

        out["tags"] = aws_sdk_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
