"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabasesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_tenant_databases_list
    import capo_rds.types.string


class DBSnapshotTenantDatabasesMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_snapshot_tenant_databases: NotRequired[
        "capo_rds.types.db_snapshot_tenant_databases_list.DBSnapshotTenantDatabasesList"
    ]
    """<p>A list of DB snapshot tenant databases.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotTenantDatabasesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_snapshot_tenant_databases" in value:
        import capo_rds.types.db_snapshot_tenant_databases_list

        capo_rds.types.db_snapshot_tenant_databases_list.serialize_query(
            value["db_snapshot_tenant_databases"],
            pairs,
            f"{key_prefix}DBSnapshotTenantDatabases",
        )


def deserialize_query(el: Element) -> DBSnapshotTenantDatabasesMessage:
    out: DBSnapshotTenantDatabasesMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_snapshot_tenant_databases = el.find("DBSnapshotTenantDatabases")
    if child_db_snapshot_tenant_databases is not None:
        import capo_rds.types.db_snapshot_tenant_databases_list

        out["db_snapshot_tenant_databases"] = (
            capo_rds.types.db_snapshot_tenant_databases_list.deserialize_query(
                child_db_snapshot_tenant_databases
            )
        )
    return out
