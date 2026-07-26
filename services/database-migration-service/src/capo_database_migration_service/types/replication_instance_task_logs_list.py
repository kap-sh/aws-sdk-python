"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstanceTaskLogsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_instance_task_log

ReplicationInstanceTaskLogsList: TypeAlias = list[
    "capo_database_migration_service.types.replication_instance_task_log.ReplicationInstanceTaskLog"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstanceTaskLogsList) -> list:
    import capo_database_migration_service.types.replication_instance_task_log

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.replication_instance_task_log.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationInstanceTaskLogsList:
    import capo_database_migration_service.types.replication_instance_task_log

    out: ReplicationInstanceTaskLogsList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.replication_instance_task_log.deserialize_aws_json_1_1(
                item
            )
        )
    return out
