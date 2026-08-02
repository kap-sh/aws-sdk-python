"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotRecycleBinInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class SnapshotRecycleBinInfo(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    recycle_bin_enter_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the snapshot is to be permanently deleted from the Recycle Bin.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume from which the snapshot was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotRecycleBinInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "recycle_bin_enter_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_enter_time"], pairs, f"{key_prefix}RecycleBinEnterTime"
        )
    if "recycle_bin_exit_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_exit_time"], pairs, f"{key_prefix}RecycleBinExitTime"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))


def deserialize_ec2_query(el: Element) -> SnapshotRecycleBinInfo:
    out: SnapshotRecycleBinInfo = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_recycle_bin_enter_time = el.find("RecycleBinEnterTime")
    if child_recycle_bin_enter_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_enter_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_enter_time
            )
        )
    child_recycle_bin_exit_time = el.find("RecycleBinExitTime")
    if child_recycle_bin_exit_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_exit_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_exit_time
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    return out
