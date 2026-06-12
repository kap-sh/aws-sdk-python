"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MoveReplicationTaskMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class MoveReplicationTaskMessage(TypedDict):
    replication_task_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the task that you want to move.</p>"""
    target_replication_instance_arn: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>The ARN of the replication instance where you want to move the task to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MoveReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    out["TargetReplicationInstanceArn"] = value["target_replication_instance_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MoveReplicationTaskMessage:
    out: MoveReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "MoveReplicationTaskMessage.replication_task_arn required"
        )
    if "TargetReplicationInstanceArn" in data:
        out["target_replication_instance_arn"] = data["TargetReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "MoveReplicationTaskMessage.target_replication_instance_arn required"
        )
    return out
