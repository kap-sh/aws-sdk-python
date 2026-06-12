"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_image

WorkspaceImageList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspace_image.WorkspaceImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageList) -> list:
    import aws_sdk_workspaces.types.workspace_image

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.workspace_image.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceImageList:
    import aws_sdk_workspaces.types.workspace_image

    out: WorkspaceImageList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.workspace_image.deserialize_aws_json_1_1(item)
        )
    return out
