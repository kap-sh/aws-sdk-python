"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabasesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_tenant_database

DBSnapshotTenantDatabasesList: TypeAlias = list[
    "capo_rds.types.db_snapshot_tenant_database.DBSnapshotTenantDatabase"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotTenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_snapshot_tenant_database

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_snapshot_tenant_database.serialize_query(
            item, pairs, f"{prefix}.DBSnapshotTenantDatabase.{n}"
        )


def deserialize_query(el: Element) -> DBSnapshotTenantDatabasesList:
    import capo_rds.types.db_snapshot_tenant_database

    out: DBSnapshotTenantDatabasesList = []
    for child in el.findall("DBSnapshotTenantDatabase"):
        out.append(capo_rds.types.db_snapshot_tenant_database.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSnapshotTenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_snapshot_tenant_database

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_snapshot_tenant_database.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBSnapshotTenantDatabasesList:
    import capo_rds.types.db_snapshot_tenant_database

    out: DBSnapshotTenantDatabasesList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_snapshot_tenant_database.deserialize_query(child))
    return out
