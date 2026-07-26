"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeTableStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.table_statistics_list


class DescribeTableStatisticsResponse(TypedDict, closed=True):
    replication_task_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication task.</p>"""
    table_statistics: NotRequired[
        "capo_database_migration_service.types.table_statistics_list.TableStatisticsList"
    ]
    """<p>The table statistics.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTableStatisticsResponse) -> dict:
    out: dict = {}
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    if "table_statistics" in value:
        import capo_database_migration_service.types.table_statistics_list

        out["TableStatistics"] = (
            capo_database_migration_service.types.table_statistics_list.serialize_aws_json_1_1(
                value["table_statistics"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTableStatisticsResponse:
    out: DescribeTableStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    if "TableStatistics" in data:
        import capo_database_migration_service.types.table_statistics_list

        out["table_statistics"] = (
            capo_database_migration_service.types.table_statistics_list.deserialize_aws_json_1_1(
                data["TableStatistics"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
