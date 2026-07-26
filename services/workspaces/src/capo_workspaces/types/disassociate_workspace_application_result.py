"""Generated from Smithy shape ``com.amazonaws.workspaces#DisassociateWorkspaceApplicationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_resource_association


class DisassociateWorkspaceApplicationResult(TypedDict, closed=True):
    association: NotRequired[
        "capo_workspaces.types.workspace_resource_association.WorkspaceResourceAssociation"
    ]
    """<p>Information about the targeted association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateWorkspaceApplicationResult) -> dict:
    out: dict = {}
    if "association" in value:
        import capo_workspaces.types.workspace_resource_association

        out["Association"] = (
            capo_workspaces.types.workspace_resource_association.serialize_aws_json_1_1(
                value["association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateWorkspaceApplicationResult:
    out: DisassociateWorkspaceApplicationResult = {}  # type: ignore[typeddict-item]
    if "Association" in data:
        import capo_workspaces.types.workspace_resource_association

        out["association"] = (
            capo_workspaces.types.workspace_resource_association.deserialize_aws_json_1_1(
                data["Association"]
            )
        )
    return out
