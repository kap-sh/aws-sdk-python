"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreTableFromClusterSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.table_restore_status


class RestoreTableFromClusterSnapshotResult(TypedDict, closed=True):
    table_restore_status: NotRequired[
        "capo_redshift.types.table_restore_status.TableRestoreStatus"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreTableFromClusterSnapshotResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "table_restore_status" in value:
        import capo_redshift.types.table_restore_status

        capo_redshift.types.table_restore_status.serialize_query(
            value["table_restore_status"], pairs, f"{key_prefix}TableRestoreStatus"
        )


def deserialize_query(el: Element) -> RestoreTableFromClusterSnapshotResult:
    out: RestoreTableFromClusterSnapshotResult = {}  # type: ignore[typeddict-item]
    child_table_restore_status = el.find("TableRestoreStatus")
    if child_table_restore_status is not None:
        import capo_redshift.types.table_restore_status

        out["table_restore_status"] = (
            capo_redshift.types.table_restore_status.deserialize_query(
                child_table_restore_status
            )
        )
    return out
