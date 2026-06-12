"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeCustomWorkspaceImageImportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_image_id


class DescribeCustomWorkspaceImageImportRequest(TypedDict):
    image_id: "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the WorkSpace image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomWorkspaceImageImportRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomWorkspaceImageImportRequest:
    out: DescribeCustomWorkspaceImageImportRequest = {}  # type: ignore[typeddict-item]
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    else:
        raise DeserializationError(
            "DescribeCustomWorkspaceImageImportRequest.image_id required"
        )
    return out
