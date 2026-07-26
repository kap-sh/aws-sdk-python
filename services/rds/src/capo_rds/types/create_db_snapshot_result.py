"""Generated from Smithy shape ``com.amazonaws.rds#CreateDBSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot


class CreateDBSnapshotResult(TypedDict, closed=True):
    db_snapshot: NotRequired["capo_rds.types.db_snapshot.DBSnapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot" in value:
        import capo_rds.types.db_snapshot

        capo_rds.types.db_snapshot.serialize_query(
            value["db_snapshot"], pairs, f"{prefix}.DBSnapshot"
        )


def deserialize_query(el: Element) -> CreateDBSnapshotResult:
    out: CreateDBSnapshotResult = {}  # type: ignore[typeddict-item]
    child_db_snapshot = el.find("DBSnapshot")
    if child_db_snapshot is not None:
        import capo_rds.types.db_snapshot

        out["db_snapshot"] = capo_rds.types.db_snapshot.deserialize_query(
            child_db_snapshot
        )
    return out
