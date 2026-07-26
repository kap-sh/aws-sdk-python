"""Generated from Smithy shape ``com.amazonaws.rds#DescribeTenantDatabasesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeTenantDatabasesMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied DB instance identifier, which must match the identifier of an existing instance owned by the Amazon Web Services account. This parameter isn't case-sensitive.</p>"""
    tenant_db_name: NotRequired["capo_rds.types.string.String"]
    """<p>The user-supplied tenant database name, which must match the name of an existing tenant database on the specified DB instance owned by your Amazon Web Services account. This parameter isn’t case-sensitive.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more database tenants to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>tenant-db-name</code> - Tenant database names. The results list only includes information about the tenant databases that match these tenant DB names.</p> </li> <li> <p> <code>tenant-database-resource-id</code> - Tenant database resource identifiers.</p> </li> <li> <p> <code>dbi-resource-id</code> - DB instance resource identifiers. The results list only includes information about the tenants contained within the DB instances identified by these resource identifiers.</p> </li> </ul>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeTenantDatabases</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeTenantDatabasesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{prefix}.DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "tenant_db_name" in value:
        pairs.append((f"{prefix}.TenantDBName", str(value["tenant_db_name"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeTenantDatabasesMessage:
    out: DescribeTenantDatabasesMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_tenant_db_name = el.find("TenantDBName")
    if child_tenant_db_name is not None:
        out["tenant_db_name"] = str(child_tenant_db_name.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
