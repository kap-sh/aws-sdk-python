"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBInstanceAutomatedBackupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_automated_backup


class DeleteDBInstanceAutomatedBackupResult(TypedDict, closed=True):
    db_instance_automated_backup: NotRequired[
        "capo_rds.types.db_instance_automated_backup.DBInstanceAutomatedBackup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBInstanceAutomatedBackupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_automated_backup" in value:
        import capo_rds.types.db_instance_automated_backup

        capo_rds.types.db_instance_automated_backup.serialize_query(
            value["db_instance_automated_backup"],
            pairs,
            f"{key_prefix}DBInstanceAutomatedBackup",
        )


def deserialize_query(el: Element) -> DeleteDBInstanceAutomatedBackupResult:
    out: DeleteDBInstanceAutomatedBackupResult = {}  # type: ignore[typeddict-item]
    child_db_instance_automated_backup = el.find("DBInstanceAutomatedBackup")
    if child_db_instance_automated_backup is not None:
        import capo_rds.types.db_instance_automated_backup

        out["db_instance_automated_backup"] = (
            capo_rds.types.db_instance_automated_backup.deserialize_query(
                child_db_instance_automated_backup
            )
        )
    return out
