"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotTierStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.snapshot_state
    import aws_sdk_ec2.types.storage_tier
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.tiering_operation_status
    import aws_sdk_ec2.types.volume_id


class SnapshotTierStatus(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume from which the snapshot was created.</p>"""
    status: NotRequired["aws_sdk_ec2.types.snapshot_state.SnapshotState"]
    """<p>The state of the snapshot.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the snapshot.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags that are assigned to the snapshot.</p>"""
    storage_tier: NotRequired["aws_sdk_ec2.types.storage_tier.StorageTier"]
    """<p>The storage tier in which the snapshot is stored. <code>standard</code> indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. <code>archive</code> indicates that the snapshot is currently archived and that it must be restored before it can be used.</p>"""
    last_tiering_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the last archive or restore process was started.</p>"""
    last_tiering_progress: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The progress of the last archive or restore process, as a percentage.</p>"""
    last_tiering_operation_status: NotRequired[
        "aws_sdk_ec2.types.tiering_operation_status.TieringOperationStatus"
    ]
    """<p>The status of the last archive or restore process.</p>"""
    last_tiering_operation_status_detail: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message describing the status of the last archive or restore process.</p>"""
    archival_complete_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the last archive process was completed.</p>"""
    restore_expiry_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotTierStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "status" in value:
        import aws_sdk_ec2.types.snapshot_state

        aws_sdk_ec2.types.snapshot_state.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "storage_tier" in value:
        import aws_sdk_ec2.types.storage_tier

        aws_sdk_ec2.types.storage_tier.serialize_ec2_query(
            value["storage_tier"], pairs, f"{prefix}.StorageTier"
        )
    if "last_tiering_start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_tiering_start_time"], pairs, f"{prefix}.LastTieringStartTime"
        )
    if "last_tiering_progress" in value:
        pairs.append(
            (f"{prefix}.LastTieringProgress", str(value["last_tiering_progress"]))
        )
    if "last_tiering_operation_status" in value:
        import aws_sdk_ec2.types.tiering_operation_status

        aws_sdk_ec2.types.tiering_operation_status.serialize_ec2_query(
            value["last_tiering_operation_status"],
            pairs,
            f"{prefix}.LastTieringOperationStatus",
        )
    if "last_tiering_operation_status_detail" in value:
        pairs.append(
            (
                f"{prefix}.LastTieringOperationStatusDetail",
                str(value["last_tiering_operation_status_detail"]),
            )
        )
    if "archival_complete_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["archival_complete_time"], pairs, f"{prefix}.ArchivalCompleteTime"
        )
    if "restore_expiry_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["restore_expiry_time"], pairs, f"{prefix}.RestoreExpiryTime"
        )


def deserialize_ec2_query(el: Element) -> SnapshotTierStatus:
    out: SnapshotTierStatus = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.snapshot_state

        out["status"] = aws_sdk_ec2.types.snapshot_state.deserialize_ec2_query(
            child_status
        )
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_storage_tier = el.find("StorageTier")
    if child_storage_tier is not None:
        import aws_sdk_ec2.types.storage_tier

        out["storage_tier"] = aws_sdk_ec2.types.storage_tier.deserialize_ec2_query(
            child_storage_tier
        )
    child_last_tiering_start_time = el.find("LastTieringStartTime")
    if child_last_tiering_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["last_tiering_start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_tiering_start_time
            )
        )
    child_last_tiering_progress = el.find("LastTieringProgress")
    if child_last_tiering_progress is not None:
        out["last_tiering_progress"] = int(child_last_tiering_progress.text or "")
    child_last_tiering_operation_status = el.find("LastTieringOperationStatus")
    if child_last_tiering_operation_status is not None:
        import aws_sdk_ec2.types.tiering_operation_status

        out["last_tiering_operation_status"] = (
            aws_sdk_ec2.types.tiering_operation_status.deserialize_ec2_query(
                child_last_tiering_operation_status
            )
        )
    child_last_tiering_operation_status_detail = el.find(
        "LastTieringOperationStatusDetail"
    )
    if child_last_tiering_operation_status_detail is not None:
        out["last_tiering_operation_status_detail"] = str(
            child_last_tiering_operation_status_detail.text or ""
        )
    child_archival_complete_time = el.find("ArchivalCompleteTime")
    if child_archival_complete_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["archival_complete_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_archival_complete_time
            )
        )
    child_restore_expiry_time = el.find("RestoreExpiryTime")
    if child_restore_expiry_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["restore_expiry_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_restore_expiry_time
            )
        )
    return out
