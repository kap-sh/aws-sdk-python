"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_automated_backup

DBInstanceAutomatedBackupList: TypeAlias = list[
    "capo_rds.types.db_instance_automated_backup.DBInstanceAutomatedBackup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_instance_automated_backup

    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_automated_backup.serialize_query(
            item, pairs, f"{prefix}.DBInstanceAutomatedBackup.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceAutomatedBackupList:
    import capo_rds.types.db_instance_automated_backup

    out: DBInstanceAutomatedBackupList = []
    for child in el.findall("DBInstanceAutomatedBackup"):
        out.append(capo_rds.types.db_instance_automated_backup.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBInstanceAutomatedBackupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_instance_automated_backup

    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_automated_backup.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBInstanceAutomatedBackupList:
    import capo_rds.types.db_instance_automated_backup

    out: DBInstanceAutomatedBackupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_instance_automated_backup.deserialize_query(child))
    return out
