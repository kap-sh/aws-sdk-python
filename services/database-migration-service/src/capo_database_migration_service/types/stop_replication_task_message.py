"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StopReplicationTaskMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class StopReplicationTaskMessage(TypedDict, closed=True):
    replication_task_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name(ARN) of the replication task to be stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopReplicationTaskMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopReplicationTaskMessage:
    out: StopReplicationTaskMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "StopReplicationTaskMessage.replication_task_arn required"
        )
    return out
