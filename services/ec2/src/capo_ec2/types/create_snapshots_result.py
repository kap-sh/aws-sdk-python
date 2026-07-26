"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.snapshot_set


class CreateSnapshotsResult(TypedDict, closed=True):
    snapshots: NotRequired["capo_ec2.types.snapshot_set.SnapshotSet"]
    """<p>List of snapshots.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSnapshotsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshots" in value:
        import capo_ec2.types.snapshot_set

        capo_ec2.types.snapshot_set.serialize_ec2_query(
            value["snapshots"], pairs, f"{prefix}.SnapshotSet"
        )


def deserialize_ec2_query(el: Element) -> CreateSnapshotsResult:
    out: CreateSnapshotsResult = {}  # type: ignore[typeddict-item]
    if el.find("SnapshotSet") is not None:
        import capo_ec2.types.snapshot_set

        out["snapshots"] = capo_ec2.types.snapshot_set.deserialize_ec2_query(
            el, "SnapshotSet"
        )
    return out
