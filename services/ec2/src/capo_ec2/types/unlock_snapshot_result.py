"""Generated from Smithy shape ``com.amazonaws.ec2#UnlockSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class UnlockSnapshotResult(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnlockSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))


def deserialize_ec2_query(el: Element) -> UnlockSnapshotResult:
    out: UnlockSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    return out
