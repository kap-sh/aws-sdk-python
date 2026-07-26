"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeReplicationsMessage(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p>Filters applied to the replications.</p> <p> Valid filter names: <code>replication-config-arn</code> | <code>replication-config-id</code> </p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationsMessage) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_database_migration_service.types.filter_list

        out["Filters"] = (
            capo_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationsMessage:
    out: DescribeReplicationsMessage = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_database_migration_service.types.filter_list

        out["filters"] = (
            capo_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
