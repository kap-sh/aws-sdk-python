"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAutomatedBackupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_automated_backup

DBClusterAutomatedBackupList: TypeAlias = list[
    "capo_rds.types.db_cluster_automated_backup.DBClusterAutomatedBackup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAutomatedBackupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_automated_backup

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_automated_backup.serialize_query(
            item, pairs, f"{prefix}.DBClusterAutomatedBackup.{n}"
        )


def deserialize_query(el: Element) -> DBClusterAutomatedBackupList:
    import capo_rds.types.db_cluster_automated_backup

    out: DBClusterAutomatedBackupList = []
    for child in el.findall("DBClusterAutomatedBackup"):
        out.append(capo_rds.types.db_cluster_automated_backup.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterAutomatedBackupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_automated_backup

    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_automated_backup.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterAutomatedBackupList:
    import capo_rds.types.db_cluster_automated_backup

    out: DBClusterAutomatedBackupList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster_automated_backup.deserialize_query(child))
    return out
