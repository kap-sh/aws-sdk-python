"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTasksMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.filter_list
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationTasksMessage(TypedDict):
    filters: NotRequired[
        "aws_sdk_database_migration_service.types.filter_list.FilterList"
    ]
    """<p>Filters applied to replication tasks.</p> <p>Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn</p>"""
    max_records: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    without_settings: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationTasksMessage) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_database_migration_service.types.filter_list

        out["Filters"] = (
            aws_sdk_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "without_settings" in value:
        out["WithoutSettings"] = value["without_settings"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationTasksMessage:
    out: DescribeReplicationTasksMessage = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_database_migration_service.types.filter_list

        out["filters"] = (
            aws_sdk_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "WithoutSettings" in data:
        out["without_settings"] = data["WithoutSettings"]
    return out
