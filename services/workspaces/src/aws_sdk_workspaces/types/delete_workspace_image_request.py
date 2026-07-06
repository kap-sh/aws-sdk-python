"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_image_id


class DeleteWorkspaceImageRequest(TypedDict, closed=True):
    image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkspaceImageRequest:
    out: DeleteWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError("DeleteWorkspaceImageRequest.image_id required")
    return out
