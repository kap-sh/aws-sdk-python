"""Generated from Smithy shape ``com.amazonaws.workspaces#StandbyWorkspacesProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.data_replication
    import capo_workspaces.types.timestamp
    import capo_workspaces.types.workspace_id


class StandbyWorkspacesProperties(TypedDict, closed=True):
    standby_workspace_id: NotRequired["capo_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the standby WorkSpace</p>"""
    data_replication: NotRequired[
        "capo_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates whether data replication is enabled, and if enabled, the type of data replication.</p>"""
    recovery_snapshot_time: NotRequired["capo_workspaces.types.timestamp.Timestamp"]
    """<p>The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StandbyWorkspacesProperties) -> dict:
    out: dict = {}
    if "standby_workspace_id" in value:
        out["StandbyWorkspaceId"] = value["standby_workspace_id"]
    if "data_replication" in value:
        import capo_workspaces.types.data_replication

        out["DataReplication"] = (
            capo_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    if "recovery_snapshot_time" in value:
        import capo_workspaces.types.timestamp

        out["RecoverySnapshotTime"] = (
            capo_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["recovery_snapshot_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StandbyWorkspacesProperties:
    out: StandbyWorkspacesProperties = {}  # type: ignore[typeddict-item]
    if "StandbyWorkspaceId" in data:
        out["standby_workspace_id"] = data["StandbyWorkspaceId"]
    if "DataReplication" in data:
        import capo_workspaces.types.data_replication

        out["data_replication"] = (
            capo_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    if "RecoverySnapshotTime" in data:
        import capo_workspaces.types.timestamp

        out["recovery_snapshot_time"] = (
            capo_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["RecoverySnapshotTime"]
            )
        )
    return out
