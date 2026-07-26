"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeDataMigrationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.marker


class DescribeDataMigrationsMessage(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p>Filters applied to the data migrations.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["capo_database_migration_service.types.marker.Marker"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    without_settings: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>"""
    without_statistics: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option to set to avoid returning information about statistics. Use this to reduce overhead when statistics information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDataMigrationsMessage) -> dict:
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
    if "without_settings" in value:
        out["WithoutSettings"] = value["without_settings"]
    if "without_statistics" in value:
        out["WithoutStatistics"] = value["without_statistics"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDataMigrationsMessage:
    out: DescribeDataMigrationsMessage = {}  # type: ignore[typeddict-item]
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
    if "WithoutSettings" in data:
        out["without_settings"] = data["WithoutSettings"]
    if "WithoutStatistics" in data:
        out["without_statistics"] = data["WithoutStatistics"]
    return out
