"""Generated from Smithy shape ``com.amazonaws.rds#DBInstanceAutomatedBackupsReplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance_automated_backups_replication

DBInstanceAutomatedBackupsReplicationList: TypeAlias = list[
    "capo_rds.types.db_instance_automated_backups_replication.DBInstanceAutomatedBackupsReplication"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBInstanceAutomatedBackupsReplicationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.db_instance_automated_backups_replication

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_automated_backups_replication.serialize_query(
            item, pairs, f"{prefix}.DBInstanceAutomatedBackupsReplication.{n}"
        )


def deserialize_query(el: Element) -> DBInstanceAutomatedBackupsReplicationList:
    import capo_rds.types.db_instance_automated_backups_replication

    out: DBInstanceAutomatedBackupsReplicationList = []
    for child in el.findall("DBInstanceAutomatedBackupsReplication"):
        out.append(
            capo_rds.types.db_instance_automated_backups_replication.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: DBInstanceAutomatedBackupsReplicationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_rds.types.db_instance_automated_backups_replication

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_instance_automated_backups_replication.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> DBInstanceAutomatedBackupsReplicationList:
    import capo_rds.types.db_instance_automated_backups_replication

    out: DBInstanceAutomatedBackupsReplicationList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.db_instance_automated_backups_replication.deserialize_query(
                child
            )
        )
    return out
