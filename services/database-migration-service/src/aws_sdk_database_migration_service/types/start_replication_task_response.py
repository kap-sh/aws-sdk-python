"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task


class StartReplicationTaskResponse(TypedDict):
    replication_task: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task.ReplicationTask"
    ]
    """<p>The replication task started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskResponse) -> dict:
    out: dict = {}
    if "replication_task" in value:
        import aws_sdk_database_migration_service.types.replication_task

        out["ReplicationTask"] = (
            aws_sdk_database_migration_service.types.replication_task.serialize_aws_json_1_1(
                value["replication_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskResponse:
    out: StartReplicationTaskResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTask" in data:
        import aws_sdk_database_migration_service.types.replication_task

        out["replication_task"] = (
            aws_sdk_database_migration_service.types.replication_task.deserialize_aws_json_1_1(
                data["ReplicationTask"]
            )
        )
    return out
