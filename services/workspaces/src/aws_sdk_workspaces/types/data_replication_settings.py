"""Generated from Smithy shape ``com.amazonaws.workspaces#DataReplicationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.data_replication
    import aws_sdk_workspaces.types.timestamp


class DataReplicationSettings(TypedDict, closed=True):
    data_replication: NotRequired[
        "aws_sdk_workspaces.types.data_replication.DataReplication"
    ]
    """<p>Indicates whether data replication is enabled, and if enabled, the type of data replication.</p>"""
    recovery_snapshot_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The date and time at which the last successful snapshot was taken of the primary WorkSpace used for replicating data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataReplicationSettings) -> dict:
    out: dict = {}
    if "data_replication" in value:
        import aws_sdk_workspaces.types.data_replication

        out["DataReplication"] = (
            aws_sdk_workspaces.types.data_replication.serialize_aws_json_1_1(
                value["data_replication"]
            )
        )
    if "recovery_snapshot_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["RecoverySnapshotTime"] = (
            aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
                value["recovery_snapshot_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataReplicationSettings:
    out: DataReplicationSettings = {}  # type: ignore[typeddict-item]
    if "DataReplication" in data:
        import aws_sdk_workspaces.types.data_replication

        out["data_replication"] = (
            aws_sdk_workspaces.types.data_replication.deserialize_aws_json_1_1(
                data["DataReplication"]
            )
        )
    if "RecoverySnapshotTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["recovery_snapshot_time"] = (
            aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
                data["RecoverySnapshotTime"]
            )
        )
    return out
