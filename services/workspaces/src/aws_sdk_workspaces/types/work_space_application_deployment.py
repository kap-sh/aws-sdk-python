"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationDeployment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_resource_association_list


class WorkSpaceApplicationDeployment(TypedDict, closed=True):
    associations: NotRequired[
        "aws_sdk_workspaces.types.workspace_resource_association_list.WorkspaceResourceAssociationList"
    ]
    """<p>The associations between the applications and the associated resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationDeployment) -> dict:
    out: dict = {}
    if "associations" in value:
        import aws_sdk_workspaces.types.workspace_resource_association_list

        out["Associations"] = (
            aws_sdk_workspaces.types.workspace_resource_association_list.serialize_aws_json_1_1(
                value["associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkSpaceApplicationDeployment:
    out: WorkSpaceApplicationDeployment = {}  # type: ignore[typeddict-item]
    if "Associations" in data:
        import aws_sdk_workspaces.types.workspace_resource_association_list

        out["associations"] = (
            aws_sdk_workspaces.types.workspace_resource_association_list.deserialize_aws_json_1_1(
                data["Associations"]
            )
        )
    return out
