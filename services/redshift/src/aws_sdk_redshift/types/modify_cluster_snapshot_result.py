"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.snapshot


class ModifyClusterSnapshotResult(TypedDict, closed=True):
    snapshot: NotRequired["aws_sdk_redshift.types.snapshot.Snapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot" in value:
        import aws_sdk_redshift.types.snapshot

        aws_sdk_redshift.types.snapshot.serialize_query(
            value["snapshot"], pairs, f"{prefix}.Snapshot"
        )


def deserialize_query(el: Element) -> ModifyClusterSnapshotResult:
    out: ModifyClusterSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot = el.find("Snapshot")
    if child_snapshot is not None:
        import aws_sdk_redshift.types.snapshot

        out["snapshot"] = aws_sdk_redshift.types.snapshot.deserialize_query(
            child_snapshot
        )
    return out
