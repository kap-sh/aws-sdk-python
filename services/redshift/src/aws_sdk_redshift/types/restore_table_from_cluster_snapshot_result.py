"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreTableFromClusterSnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.table_restore_status


class RestoreTableFromClusterSnapshotResult(TypedDict):
    table_restore_status: NotRequired[
        "aws_sdk_redshift.types.table_restore_status.TableRestoreStatus"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreTableFromClusterSnapshotResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "table_restore_status" in value:
        import aws_sdk_redshift.types.table_restore_status

        aws_sdk_redshift.types.table_restore_status.serialize_query(
            value["table_restore_status"], pairs, f"{prefix}.TableRestoreStatus"
        )


def deserialize_query(el: Element) -> RestoreTableFromClusterSnapshotResult:
    out: RestoreTableFromClusterSnapshotResult = {}  # type: ignore[typeddict-item]
    child_table_restore_status = el.find("TableRestoreStatus")
    if child_table_restore_status is not None:
        import aws_sdk_redshift.types.table_restore_status

        out["table_restore_status"] = (
            aws_sdk_redshift.types.table_restore_status.deserialize_query(
                child_table_restore_status
            )
        )
    return out
