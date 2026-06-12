"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterAutomatedBackupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_automated_backup


class DeleteDBClusterAutomatedBackupResult(TypedDict):
    db_cluster_automated_backup: NotRequired[
        "aws_sdk_rds.types.db_cluster_automated_backup.DBClusterAutomatedBackup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterAutomatedBackupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_automated_backup" in value:
        import aws_sdk_rds.types.db_cluster_automated_backup

        aws_sdk_rds.types.db_cluster_automated_backup.serialize_query(
            value["db_cluster_automated_backup"],
            pairs,
            f"{prefix}.DBClusterAutomatedBackup",
        )


def deserialize_query(el: Element) -> DeleteDBClusterAutomatedBackupResult:
    out: DeleteDBClusterAutomatedBackupResult = {}  # type: ignore[typeddict-item]
    child_db_cluster_automated_backup = el.find("DBClusterAutomatedBackup")
    if child_db_cluster_automated_backup is not None:
        import aws_sdk_rds.types.db_cluster_automated_backup

        out["db_cluster_automated_backup"] = (
            aws_sdk_rds.types.db_cluster_automated_backup.deserialize_query(
                child_db_cluster_automated_backup
            )
        )
    return out
