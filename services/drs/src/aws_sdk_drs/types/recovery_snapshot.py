"""Generated from Smithy shape ``com.amazonaws.drs#RecoverySnapshot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.ebs_snapshots_list
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.recovery_snapshot_id
    import aws_sdk_drs.types.source_server_id


class RecoverySnapshot(TypedDict):
    snapshot_id: "aws_sdk_drs.types.recovery_snapshot_id.RecoverySnapshotID"
    """<p>The ID of the Recovery Snapshot.</p>"""
    source_server_id: "aws_sdk_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server that the snapshot was taken for.</p>"""
    expected_timestamp: (
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    )
    """<p>The timestamp of when we expect the snapshot to be taken.</p>"""
    timestamp: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The actual timestamp that the snapshot was taken.</p>"""
    ebs_snapshots: NotRequired["aws_sdk_drs.types.ebs_snapshots_list.EbsSnapshotsList"]
    """<p>A list of EBS snapshots.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoverySnapshot) -> dict:
    out: dict = {}
    out["snapshotID"] = value["snapshot_id"]
    out["sourceServerID"] = value["source_server_id"]
    out["expectedTimestamp"] = value["expected_timestamp"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "ebs_snapshots" in value:
        import aws_sdk_drs.types.ebs_snapshots_list

        out["ebsSnapshots"] = aws_sdk_drs.types.ebs_snapshots_list.serialize_json(
            value["ebs_snapshots"]
        )
    return out


def deserialize_json(data: dict) -> RecoverySnapshot:
    out: RecoverySnapshot = {}  # type: ignore[typeddict-item]
    if "snapshotID" in data:
        out["snapshot_id"] = data["snapshotID"]
    else:
        raise DeserializationError("RecoverySnapshot.snapshot_id required")
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("RecoverySnapshot.source_server_id required")
    if "expectedTimestamp" in data:
        out["expected_timestamp"] = data["expectedTimestamp"]
    else:
        raise DeserializationError("RecoverySnapshot.expected_timestamp required")
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "ebsSnapshots" in data:
        import aws_sdk_drs.types.ebs_snapshots_list

        out["ebs_snapshots"] = aws_sdk_drs.types.ebs_snapshots_list.deserialize_json(
            data["ebsSnapshots"]
        )
    return out
