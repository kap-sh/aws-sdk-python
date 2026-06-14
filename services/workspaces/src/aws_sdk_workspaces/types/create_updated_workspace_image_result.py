"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateUpdatedWorkspaceImageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_image_id


class CreateUpdatedWorkspaceImageResult(TypedDict):
    image_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    ]
    """<p>The identifier of the new updated WorkSpace image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedWorkspaceImageResult:
    out: CreateUpdatedWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    return out
