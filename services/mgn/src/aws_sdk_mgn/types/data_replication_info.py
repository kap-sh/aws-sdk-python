"""Generated from Smithy shape ``com.amazonaws.mgn#DataReplicationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.data_replication_error
    import aws_sdk_mgn.types.data_replication_info_replicated_disks
    import aws_sdk_mgn.types.data_replication_initiation
    import aws_sdk_mgn.types.data_replication_state
    import aws_sdk_mgn.types.iso8601_datetime_string
    import aws_sdk_mgn.types.iso8601_duration_string
    import aws_sdk_mgn.types.replicator_id


class DataReplicationInfo(TypedDict):
    lag_duration: NotRequired[
        "aws_sdk_mgn.types.iso8601_duration_string.ISO8601DurationString"
    ]
    """<p>Request to query data replication lag duration.</p>"""
    eta_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query the time when data replication will be complete.</p>"""
    replicated_disks: NotRequired[
        "aws_sdk_mgn.types.data_replication_info_replicated_disks.DataReplicationInfoReplicatedDisks"
    ]
    """<p>Request to query disks replicated.</p>"""
    data_replication_state: NotRequired[
        "aws_sdk_mgn.types.data_replication_state.DataReplicationState"
    ]
    """<p>Request to query the data replication state.</p>"""
    data_replication_initiation: NotRequired[
        "aws_sdk_mgn.types.data_replication_initiation.DataReplicationInitiation"
    ]
    """<p>Request to query whether data replication has been initiated.</p>"""
    data_replication_error: NotRequired[
        "aws_sdk_mgn.types.data_replication_error.DataReplicationError"
    ]
    """<p>Error in obtaining data replication info.</p>"""
    last_snapshot_date_time: NotRequired[
        "aws_sdk_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Request to query data replication last snapshot time.</p>"""
    replicator_id: NotRequired["aws_sdk_mgn.types.replicator_id.ReplicatorID"]
    """<p>Replication server instance ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationInfo) -> dict:
    out: dict = {}
    if "lag_duration" in value:
        out["lagDuration"] = value["lag_duration"]
    if "eta_date_time" in value:
        out["etaDateTime"] = value["eta_date_time"]
    if "replicated_disks" in value:
        import aws_sdk_mgn.types.data_replication_info_replicated_disks

        out["replicatedDisks"] = (
            aws_sdk_mgn.types.data_replication_info_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
    if "data_replication_state" in value:
        out["dataReplicationState"] = value["data_replication_state"]
    if "data_replication_initiation" in value:
        import aws_sdk_mgn.types.data_replication_initiation

        out["dataReplicationInitiation"] = (
            aws_sdk_mgn.types.data_replication_initiation.serialize_json(
                value["data_replication_initiation"]
            )
        )
    if "data_replication_error" in value:
        import aws_sdk_mgn.types.data_replication_error

        out["dataReplicationError"] = (
            aws_sdk_mgn.types.data_replication_error.serialize_json(
                value["data_replication_error"]
            )
        )
    if "last_snapshot_date_time" in value:
        out["lastSnapshotDateTime"] = value["last_snapshot_date_time"]
    if "replicator_id" in value:
        out["replicatorId"] = value["replicator_id"]
    return out


def deserialize_json(data: dict) -> DataReplicationInfo:
    out: DataReplicationInfo = {}  # type: ignore[typeddict-item]
    if "lagDuration" in data:
        out["lag_duration"] = data["lagDuration"]
    if "etaDateTime" in data:
        out["eta_date_time"] = data["etaDateTime"]
    if "replicatedDisks" in data:
        import aws_sdk_mgn.types.data_replication_info_replicated_disks

        out["replicated_disks"] = (
            aws_sdk_mgn.types.data_replication_info_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
    if "dataReplicationState" in data:
        out["data_replication_state"] = data["dataReplicationState"]
    if "dataReplicationInitiation" in data:
        import aws_sdk_mgn.types.data_replication_initiation

        out["data_replication_initiation"] = (
            aws_sdk_mgn.types.data_replication_initiation.deserialize_json(
                data["dataReplicationInitiation"]
            )
        )
    if "dataReplicationError" in data:
        import aws_sdk_mgn.types.data_replication_error

        out["data_replication_error"] = (
            aws_sdk_mgn.types.data_replication_error.deserialize_json(
                data["dataReplicationError"]
            )
        )
    if "lastSnapshotDateTime" in data:
        out["last_snapshot_date_time"] = data["lastSnapshotDateTime"]
    if "replicatorId" in data:
        out["replicator_id"] = data["replicatorId"]
    return out
