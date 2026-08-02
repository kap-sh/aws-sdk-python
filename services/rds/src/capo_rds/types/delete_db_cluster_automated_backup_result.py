"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterAutomatedBackupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_automated_backup


class DeleteDBClusterAutomatedBackupResult(TypedDict, closed=True):
    db_cluster_automated_backup: NotRequired[
        "capo_rds.types.db_cluster_automated_backup.DBClusterAutomatedBackup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterAutomatedBackupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_automated_backup" in value:
        import capo_rds.types.db_cluster_automated_backup

        capo_rds.types.db_cluster_automated_backup.serialize_query(
            value["db_cluster_automated_backup"],
            pairs,
            f"{key_prefix}DBClusterAutomatedBackup",
        )


def deserialize_query(el: Element) -> DeleteDBClusterAutomatedBackupResult:
    out: DeleteDBClusterAutomatedBackupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_automated_backup = el.find("DBClusterAutomatedBackup")
    if child_db_cluster_automated_backup is not None:
        import capo_rds.types.db_cluster_automated_backup

        out["db_cluster_automated_backup"] = (
            capo_rds.types.db_cluster_automated_backup.deserialize_query(
                child_db_cluster_automated_backup
            )
        )
    return out
