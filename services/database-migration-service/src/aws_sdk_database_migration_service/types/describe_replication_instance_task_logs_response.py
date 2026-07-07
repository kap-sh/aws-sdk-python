"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationInstanceTaskLogsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_instance_task_logs_list
    import aws_sdk_database_migration_service.types.string


class DescribeReplicationInstanceTaskLogsResponse(TypedDict, closed=True):
    replication_instance_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication instance.</p>"""
    replication_instance_task_logs: NotRequired[
        "aws_sdk_database_migration_service.types.replication_instance_task_logs_list.ReplicationInstanceTaskLogsList"
    ]
    """<p>An array of replication task log metadata. Each member of the array contains the replication task name, ARN, and task log size (in bytes). </p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationInstanceTaskLogsResponse) -> dict:
    out: dict = {}
    if "replication_instance_arn" in value:
        out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    if "replication_instance_task_logs" in value:
        import aws_sdk_database_migration_service.types.replication_instance_task_logs_list

        out["ReplicationInstanceTaskLogs"] = (
            aws_sdk_database_migration_service.types.replication_instance_task_logs_list.serialize_aws_json_1_1(
                value["replication_instance_task_logs"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationInstanceTaskLogsResponse:
    out: DescribeReplicationInstanceTaskLogsResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    if "ReplicationInstanceTaskLogs" in data:
        import aws_sdk_database_migration_service.types.replication_instance_task_logs_list

        out["replication_instance_task_logs"] = (
            aws_sdk_database_migration_service.types.replication_instance_task_logs_list.deserialize_aws_json_1_1(
                data["ReplicationInstanceTaskLogs"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
