"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateReplicationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task


class CreateReplicationTaskResponse(TypedDict, closed=True):
    replication_task: NotRequired[
        "capo_database_migration_service.types.replication_task.ReplicationTask"
    ]
    """<p>The replication task that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateReplicationTaskResponse) -> dict:
    out: dict = {}
    if "replication_task" in value:
        import capo_database_migration_service.types.replication_task

        out["ReplicationTask"] = (
            capo_database_migration_service.types.replication_task.serialize_aws_json_1_1(
                value["replication_task"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateReplicationTaskResponse:
    out: CreateReplicationTaskResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTask" in data:
        import capo_database_migration_service.types.replication_task

        out["replication_task"] = (
            capo_database_migration_service.types.replication_task.deserialize_aws_json_1_1(
                data["ReplicationTask"]
            )
        )
    return out
