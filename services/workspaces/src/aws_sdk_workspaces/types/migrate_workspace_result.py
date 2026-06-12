"""Generated from Smithy shape ``com.amazonaws.workspaces#MigrateWorkspaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_id


class MigrateWorkspaceResult(TypedDict):
    source_workspace_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    ]
    """<p>The original identifier of the WorkSpace that is being migrated.</p>"""
    target_workspace_id: NotRequired[
        "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    ]
    """<p>The new identifier of the WorkSpace that is being migrated. If the migration does not succeed, the target WorkSpace ID will not be used, and the WorkSpace will still have the original WorkSpace ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrateWorkspaceResult) -> dict:
    out: dict = {}
    if "source_workspace_id" in value:
        out["SourceWorkspaceId"] = value["source_workspace_id"]
    if "target_workspace_id" in value:
        out["TargetWorkspaceId"] = value["target_workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrateWorkspaceResult:
    out: MigrateWorkspaceResult = {}  # type: ignore[typeddict-item]
    if "SourceWorkspaceId" in data:
        out["source_workspace_id"] = data["SourceWorkspaceId"]
    if "TargetWorkspaceId" in data:
        out["target_workspace_id"] = data["TargetWorkspaceId"]
    return out
