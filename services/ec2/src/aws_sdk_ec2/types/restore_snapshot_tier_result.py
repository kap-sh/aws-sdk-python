"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotTierResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class RestoreSnapshotTierResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    restore_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot restore process started.</p>"""
    restore_duration: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>For temporary restores only. The number of days for which the archived snapshot is temporarily restored.</p>"""
    is_permanent_restore: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is permanently restored. <code>true</code> indicates a permanent restore. <code>false</code> indicates a temporary restore.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreSnapshotTierResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "restore_start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["restore_start_time"], pairs, f"{prefix}.RestoreStartTime"
        )
    if "restore_duration" in value:
        pairs.append((f"{prefix}.RestoreDuration", str(value["restore_duration"])))
    if "is_permanent_restore" in value:
        pairs.append(
            (
                f"{prefix}.IsPermanentRestore",
                "true" if value["is_permanent_restore"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> RestoreSnapshotTierResult:
    out: RestoreSnapshotTierResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_restore_start_time = el.find("RestoreStartTime")
    if child_restore_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["restore_start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_restore_start_time
            )
        )
    child_restore_duration = el.find("RestoreDuration")
    if child_restore_duration is not None:
        out["restore_duration"] = int(child_restore_duration.text or "")
    child_is_permanent_restore = el.find("IsPermanentRestore")
    if child_is_permanent_restore is not None:
        out["is_permanent_restore"] = (
            child_is_permanent_restore.text or ""
        ).lower() == "true"
    return out
