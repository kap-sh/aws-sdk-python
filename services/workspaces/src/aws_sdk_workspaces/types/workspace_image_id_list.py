"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_image_id

WorkspaceImageIdList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspace_image_id.WorkspaceImageId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkspaceImageIdList:
    return list(data)
