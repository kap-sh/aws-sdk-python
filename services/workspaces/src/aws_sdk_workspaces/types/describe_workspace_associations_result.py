"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_resource_association_list


class DescribeWorkspaceAssociationsResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_workspaces.types.workspace_resource_association_list.WorkspaceResourceAssociationList"
    ]
    """<p>List of information about the specified associations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceAssociationsResult) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_workspaces.types.workspace_resource_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.workspace_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceAssociationsResult:
    out: DescribeWorkspaceAssociationsResult = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_workspaces.types.workspace_resource_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.workspace_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
