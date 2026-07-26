"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task_list
    import capo_database_migration_service.types.string


class DescribeReplicationTasksResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    replication_tasks: NotRequired[
        "capo_database_migration_service.types.replication_task_list.ReplicationTaskList"
    ]
    """<p>A description of the replication tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationTasksResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "replication_tasks" in value:
        import capo_database_migration_service.types.replication_task_list

        out["ReplicationTasks"] = (
            capo_database_migration_service.types.replication_task_list.serialize_aws_json_1_1(
                value["replication_tasks"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationTasksResponse:
    out: DescribeReplicationTasksResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ReplicationTasks" in data:
        import capo_database_migration_service.types.replication_task_list

        out["replication_tasks"] = (
            capo_database_migration_service.types.replication_task_list.deserialize_aws_json_1_1(
                data["ReplicationTasks"]
            )
        )
    return out
