"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#UpdateWorkspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.description
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.role_arn
    import aws_sdk_iottwinmaker.types.s3_location


class UpdateWorkspaceRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace.</p>"""
    description: NotRequired["aws_sdk_iottwinmaker.types.description.Description"]
    """<p>The description of the workspace.</p>"""
    role: NotRequired["aws_sdk_iottwinmaker.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role associated with the workspace.</p>"""
    s3_location: NotRequired["aws_sdk_iottwinmaker.types.s3_location.S3Location"]
    """<p>The ARN of the S3 bucket where resources associated with the workspace are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "role" in value:
        out["role"] = value["role"]
    if "s3_location" in value:
        out["s3Location"] = value["s3_location"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceRequest:
    out: UpdateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "role" in data:
        out["role"] = data["role"]
    if "s3Location" in data:
        out["s3_location"] = data["s3Location"]
    return out
