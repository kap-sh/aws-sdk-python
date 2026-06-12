"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotTenantDatabasesMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_snapshot_tenant_databases_list
    import aws_sdk_rds.types.string


class DBSnapshotTenantDatabasesMessage(TypedDict):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_snapshot_tenant_databases: NotRequired[
        "aws_sdk_rds.types.db_snapshot_tenant_databases_list.DBSnapshotTenantDatabasesList"
    ]
    """<p>A list of DB snapshot tenant databases.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotTenantDatabasesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_snapshot_tenant_databases" in value:
        import aws_sdk_rds.types.db_snapshot_tenant_databases_list

        aws_sdk_rds.types.db_snapshot_tenant_databases_list.serialize_query(
            value["db_snapshot_tenant_databases"],
            pairs,
            f"{prefix}.DBSnapshotTenantDatabases",
        )


def deserialize_query(el: Element) -> DBSnapshotTenantDatabasesMessage:
    out: DBSnapshotTenantDatabasesMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_snapshot_tenant_databases = el.find("DBSnapshotTenantDatabases")
    if child_db_snapshot_tenant_databases is not None:
        import aws_sdk_rds.types.db_snapshot_tenant_databases_list

        out["db_snapshot_tenant_databases"] = (
            aws_sdk_rds.types.db_snapshot_tenant_databases_list.deserialize_query(
                child_db_snapshot_tenant_databases
            )
        )
    return out
