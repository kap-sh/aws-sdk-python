"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskAssessmentMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class StartReplicationTaskAssessmentMessage(TypedDict):
    replication_task_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p> The Amazon Resource Name (ARN) of the replication task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskAssessmentMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskArn"] = value["replication_task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskAssessmentMessage:
    out: StartReplicationTaskAssessmentMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    else:
        raise DeserializationError(
            "StartReplicationTaskAssessmentMessage.replication_task_arn required"
        )
    return out
