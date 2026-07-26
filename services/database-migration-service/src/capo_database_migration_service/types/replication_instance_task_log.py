"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationInstanceTaskLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.long
    import capo_database_migration_service.types.string


class ReplicationInstanceTaskLog(TypedDict, closed=True):
    replication_task_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the replication task.</p>"""
    replication_task_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication task.</p>"""
    replication_instance_task_log_size: (
        "capo_database_migration_service.types.long.Long"
    )
    """<p>The size, in bytes, of the replication task log.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationInstanceTaskLog) -> dict:
    out: dict = {}
    if "replication_task_name" in value:
        out["ReplicationTaskName"] = value["replication_task_name"]
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    out["ReplicationInstanceTaskLogSize"] = value.get(
        "replication_instance_task_log_size", 0
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationInstanceTaskLog:
    out: ReplicationInstanceTaskLog = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskName" in data:
        out["replication_task_name"] = data["ReplicationTaskName"]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    if "ReplicationInstanceTaskLogSize" in data:
        out["replication_instance_task_log_size"] = data[
            "ReplicationInstanceTaskLogSize"
        ]
    else:
        out["replication_instance_task_log_size"] = 0
    return out
