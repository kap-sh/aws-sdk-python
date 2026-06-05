"""Generated from Smithy shape ``com.amazonaws.ec2#UnlockSnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class UnlockSnapshotResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnlockSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))


def deserialize_ec2_query(el: Element) -> UnlockSnapshotResult:
    out: UnlockSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    return out
