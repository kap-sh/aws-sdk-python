"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.role_arn
    import aws_sdk_iottwinmaker.types.s3_location
    import aws_sdk_iottwinmaker.types.tag_map


class CreateWorkspaceRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the workspace.</p>"""
    s3_location: NotRequired["aws_sdk_iottwinmaker.types.s3_location.S3Location"]
    """<p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>"""
    role: NotRequired["aws_sdk_iottwinmaker.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role associated with the workspace.</p>"""
    tags: NotRequired["aws_sdk_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage the workspace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "s3_location" in value:
        out["s3Location"] = value["s3_location"]
    if "role" in value:
        out["role"] = value["role"]
    if "tags" in value:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateWorkspaceRequest:
    out: CreateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "s3Location" in data:
        out["s3_location"] = data["s3Location"]
    if "role" in data:
        out["role"] = data["role"]
    if "tags" in data:
        import aws_sdk_iottwinmaker.types.tag_map

        out["tags"] = aws_sdk_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    return out
