"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_resource_association

WorkspaceResourceAssociationList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspace_resource_association.WorkspaceResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceResourceAssociationList) -> list:
    import aws_sdk_workspaces.types.workspace_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.workspace_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WorkspaceResourceAssociationList:
    import aws_sdk_workspaces.types.workspace_resource_association

    out: WorkspaceResourceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.workspace_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
