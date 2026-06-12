"""Generated from Smithy shape ``com.amazonaws.workspaces#RelatedWorkspaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.related_workspace_properties

RelatedWorkspaces: TypeAlias = list[
    "aws_sdk_workspaces.types.related_workspace_properties.RelatedWorkspaceProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedWorkspaces) -> list:
    import aws_sdk_workspaces.types.related_workspace_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.related_workspace_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelatedWorkspaces:
    import aws_sdk_workspaces.types.related_workspace_properties

    out: RelatedWorkspaces = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.related_workspace_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
