"""Generated from Smithy shape ``com.amazonaws.workspaces#MigrateWorkspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_id
    import aws_sdk_workspaces.types.workspace_id


class MigrateWorkspaceRequest(TypedDict):
    source_workspace_id: "aws_sdk_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace to migrate from.</p>"""
    bundle_id: "aws_sdk_workspaces.types.bundle_id.BundleId"
    """<p>The identifier of the target bundle type to migrate the WorkSpace to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrateWorkspaceRequest) -> dict:
    out: dict = {}
    out["SourceWorkspaceId"] = value["source_workspace_id"]
    out["BundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrateWorkspaceRequest:
    out: MigrateWorkspaceRequest = {}  # type: ignore[typeddict-item]
    if "SourceWorkspaceId" in data:
        out["source_workspace_id"] = data["SourceWorkspaceId"]
    else:
        raise DeserializationError(
            "MigrateWorkspaceRequest.source_workspace_id required"
        )
    if "BundleId" in data:
        out["bundle_id"] = data["BundleId"]
    else:
        raise DeserializationError("MigrateWorkspaceRequest.bundle_id required")
    return out
