"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disable_fast_snapshot_restore_state_error_set
    import capo_ec2.types.string


class DisableFastSnapshotRestoreErrorItem(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    fast_snapshot_restore_state_errors: NotRequired[
        "capo_ec2.types.disable_fast_snapshot_restore_state_error_set.DisableFastSnapshotRestoreStateErrorSet"
    ]
    """<p>The errors.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoreErrorItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "fast_snapshot_restore_state_errors" in value:
        import capo_ec2.types.disable_fast_snapshot_restore_state_error_set

        capo_ec2.types.disable_fast_snapshot_restore_state_error_set.serialize_ec2_query(
            value["fast_snapshot_restore_state_errors"],
            pairs,
            f"{key_prefix}FastSnapshotRestoreStateErrorSet",
        )


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoreErrorItem:
    out: DisableFastSnapshotRestoreErrorItem = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    if el.find("fastSnapshotRestoreStateErrorSet") is not None:
        import capo_ec2.types.disable_fast_snapshot_restore_state_error_set

        out["fast_snapshot_restore_state_errors"] = (
            capo_ec2.types.disable_fast_snapshot_restore_state_error_set.deserialize_ec2_query(
                el, "fastSnapshotRestoreStateErrorSet"
            )
        )
    return out
