"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set
    import aws_sdk_ec2.types.string


class EnableFastSnapshotRestoreErrorItem(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    fast_snapshot_restore_state_errors: NotRequired[
        "aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set.EnableFastSnapshotRestoreStateErrorSet"
    ]
    """<p>The errors.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoreErrorItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "fast_snapshot_restore_state_errors" in value:
        import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set

        aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set.serialize_ec2_query(
            value["fast_snapshot_restore_state_errors"],
            pairs,
            f"{prefix}.FastSnapshotRestoreStateErrorSet",
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoreErrorItem:
    out: EnableFastSnapshotRestoreErrorItem = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    if el.find("FastSnapshotRestoreStateErrorSet") is not None:
        import aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set

        out["fast_snapshot_restore_state_errors"] = (
            aws_sdk_ec2.types.enable_fast_snapshot_restore_state_error_set.deserialize_ec2_query(
                el, "FastSnapshotRestoreStateErrorSet"
            )
        )
    return out
