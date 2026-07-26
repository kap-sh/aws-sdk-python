"""Generated from Smithy shape ``com.amazonaws.workspaces#RelatedWorkspaceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.region
    import capo_workspaces.types.standby_workspace_relationship_type
    import capo_workspaces.types.workspace_id
    import capo_workspaces.types.workspace_state


class RelatedWorkspaceProperties(TypedDict, closed=True):
    workspace_id: NotRequired["capo_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the related WorkSpace.</p>"""
    region: NotRequired["capo_workspaces.types.region.Region"]
    """<p>The Region of the related WorkSpace.</p>"""
    state: NotRequired["capo_workspaces.types.workspace_state.WorkspaceState"]
    """<p>Indicates the state of the WorkSpace.</p>"""
    type: NotRequired[
        "capo_workspaces.types.standby_workspace_relationship_type.StandbyWorkspaceRelationshipType"
    ]
    """<p>Indicates the type of WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedWorkspaceProperties) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    if "region" in value:
        out["Region"] = value["region"]
    if "state" in value:
        import capo_workspaces.types.workspace_state

        out["State"] = capo_workspaces.types.workspace_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "type" in value:
        import capo_workspaces.types.standby_workspace_relationship_type

        out["Type"] = (
            capo_workspaces.types.standby_workspace_relationship_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelatedWorkspaceProperties:
    out: RelatedWorkspaceProperties = {}  # type: ignore[typeddict-item]
    if "WorkspaceId" in data:
        out["workspace_id"] = data["WorkspaceId"]
    if "Region" in data:
        out["region"] = data["Region"]
    if "State" in data:
        import capo_workspaces.types.workspace_state

        out["state"] = capo_workspaces.types.workspace_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Type" in data:
        import capo_workspaces.types.standby_workspace_relationship_type

        out["type"] = (
            capo_workspaces.types.standby_workspace_relationship_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
