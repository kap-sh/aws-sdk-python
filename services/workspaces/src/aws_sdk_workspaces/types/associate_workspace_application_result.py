"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociateWorkspaceApplicationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_resource_association


class AssociateWorkspaceApplicationResult(TypedDict):
    association: NotRequired[
        "aws_sdk_workspaces.types.workspace_resource_association.WorkspaceResourceAssociation"
    ]
    """<p>Information about the association between the specified WorkSpace and the specified application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWorkspaceApplicationResult) -> dict:
    out: dict = {}
    if "association" in value:
        import aws_sdk_workspaces.types.workspace_resource_association

        out["Association"] = (
            aws_sdk_workspaces.types.workspace_resource_association.serialize_aws_json_1_1(
                value["association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWorkspaceApplicationResult:
    out: AssociateWorkspaceApplicationResult = {}  # type: ignore[typeddict-item]
    if "Association" in data:
        import aws_sdk_workspaces.types.workspace_resource_association

        out["association"] = (
            aws_sdk_workspaces.types.workspace_resource_association.deserialize_aws_json_1_1(
                data["Association"]
            )
        )
    return out
