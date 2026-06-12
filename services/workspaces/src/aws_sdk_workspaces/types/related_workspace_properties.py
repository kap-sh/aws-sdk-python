"""Generated from Smithy shape ``com.amazonaws.workspaces#RelatedWorkspaceProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.region
    import aws_sdk_workspaces.types.standby_workspace_relationship_type
    import aws_sdk_workspaces.types.workspace_id
    import aws_sdk_workspaces.types.workspace_state


class RelatedWorkspaceProperties(TypedDict):
    workspace_id: NotRequired["aws_sdk_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the related WorkSpace.</p>"""
    region: NotRequired["aws_sdk_workspaces.types.region.Region"]
    """<p>The Region of the related WorkSpace.</p>"""
    state: NotRequired["aws_sdk_workspaces.types.workspace_state.WorkspaceState"]
    """<p>Indicates the state of the WorkSpace.</p>"""
    type: NotRequired[
        "aws_sdk_workspaces.types.standby_workspace_relationship_type.StandbyWorkspaceRelationshipType"
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
        import aws_sdk_workspaces.types.workspace_state

        out["State"] = aws_sdk_workspaces.types.workspace_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "type" in value:
        import aws_sdk_workspaces.types.standby_workspace_relationship_type

        out["Type"] = (
            aws_sdk_workspaces.types.standby_workspace_relationship_type.serialize_aws_json_1_1(
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
        import aws_sdk_workspaces.types.workspace_state

        out["state"] = (
            aws_sdk_workspaces.types.workspace_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "Type" in data:
        import aws_sdk_workspaces.types.standby_workspace_relationship_type

        out["type"] = (
            aws_sdk_workspaces.types.standby_workspace_relationship_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
