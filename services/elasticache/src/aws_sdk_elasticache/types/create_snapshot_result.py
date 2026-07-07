"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.snapshot


class CreateSnapshotResult(TypedDict, closed=True):
    snapshot: NotRequired["aws_sdk_elasticache.types.snapshot.Snapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot" in value:
        import aws_sdk_elasticache.types.snapshot

        aws_sdk_elasticache.types.snapshot.serialize_query(
            value["snapshot"], pairs, f"{prefix}.Snapshot"
        )


def deserialize_query(el: Element) -> CreateSnapshotResult:
    out: CreateSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot = el.find("Snapshot")
    if child_snapshot is not None:
        import aws_sdk_elasticache.types.snapshot

        out["snapshot"] = aws_sdk_elasticache.types.snapshot.deserialize_query(
            child_snapshot
        )
    return out
