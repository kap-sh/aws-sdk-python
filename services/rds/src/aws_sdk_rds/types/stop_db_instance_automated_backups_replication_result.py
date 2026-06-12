"""Generated from Smithy shape ``com.amazonaws.rds#StopDBInstanceAutomatedBackupsReplicationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_instance_automated_backup


class StopDBInstanceAutomatedBackupsReplicationResult(TypedDict):
    db_instance_automated_backup: NotRequired[
        "aws_sdk_rds.types.db_instance_automated_backup.DBInstanceAutomatedBackup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: StopDBInstanceAutomatedBackupsReplicationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_instance_automated_backup" in value:
        import aws_sdk_rds.types.db_instance_automated_backup

        aws_sdk_rds.types.db_instance_automated_backup.serialize_query(
            value["db_instance_automated_backup"],
            pairs,
            f"{prefix}.DBInstanceAutomatedBackup",
        )


def deserialize_query(el: Element) -> StopDBInstanceAutomatedBackupsReplicationResult:
    out: StopDBInstanceAutomatedBackupsReplicationResult = {}  # type: ignore[typeddict-item]
    child_db_instance_automated_backup = el.find("DBInstanceAutomatedBackup")
    if child_db_instance_automated_backup is not None:
        import aws_sdk_rds.types.db_instance_automated_backup

        out["db_instance_automated_backup"] = (
            aws_sdk_rds.types.db_instance_automated_backup.deserialize_query(
                child_db_instance_automated_backup
            )
        )
    return out
