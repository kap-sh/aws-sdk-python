"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.snapshot


class ModifyClusterSnapshotResult(TypedDict, closed=True):
    snapshot: NotRequired["capo_redshift.types.snapshot.Snapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot" in value:
        import capo_redshift.types.snapshot

        capo_redshift.types.snapshot.serialize_query(
            value["snapshot"], pairs, f"{key_prefix}Snapshot"
        )


def deserialize_query(el: Element) -> ModifyClusterSnapshotResult:
    out: ModifyClusterSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot = el.find("Snapshot")
    if child_snapshot is not None:
        import capo_redshift.types.snapshot

        out["snapshot"] = capo_redshift.types.snapshot.deserialize_query(child_snapshot)
    return out
