"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTableStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_table_statistics_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationTableStatisticsResponse(TypedDict, closed=True):
    replication_config_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name of the replication config.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replication_table_statistics: NotRequired[
        "aws_sdk_database_migration_service.types.replication_table_statistics_list.ReplicationTableStatisticsList"
    ]
    """<p>Returns table statistics on the replication, including table name, rows inserted, rows updated, and rows deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationTableStatisticsResponse) -> dict:
    out: dict = {}
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_table_statistics" in value:
        import aws_sdk_database_migration_service.types.replication_table_statistics_list

        out["ReplicationTableStatistics"] = (
            aws_sdk_database_migration_service.types.replication_table_statistics_list.serialize_aws_json_1_1(
                value["replication_table_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationTableStatisticsResponse:
    out: DescribeReplicationTableStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationTableStatistics" in data:
        import aws_sdk_database_migration_service.types.replication_table_statistics_list

        out["replication_table_statistics"] = (
            aws_sdk_database_migration_service.types.replication_table_statistics_list.deserialize_aws_json_1_1(
                data["ReplicationTableStatistics"]
            )
        )
    return out
