"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task

ReplicationTaskList: TypeAlias = list[
    "capo_database_migration_service.types.replication_task.ReplicationTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskList) -> list:
    import capo_database_migration_service.types.replication_task

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.replication_task.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationTaskList:
    import capo_database_migration_service.types.replication_task

    out: ReplicationTaskList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.replication_task.deserialize_aws_json_1_1(
                item
            )
        )
    return out
