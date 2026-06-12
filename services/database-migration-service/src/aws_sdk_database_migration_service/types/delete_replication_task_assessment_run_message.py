"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DeleteReplicationTaskAssessmentRunMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class DeleteReplicationTaskAssessmentRunMessage(TypedDict):
    replication_task_assessment_run_arn: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>Amazon Resource Name (ARN) of the premigration assessment run to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReplicationTaskAssessmentRunMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskAssessmentRunArn"] = value[
        "replication_task_assessment_run_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReplicationTaskAssessmentRunMessage:
    out: DeleteReplicationTaskAssessmentRunMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskAssessmentRunArn" in data:
        out["replication_task_assessment_run_arn"] = data[
            "ReplicationTaskAssessmentRunArn"
        ]
    else:
        raise DeserializationError(
            "DeleteReplicationTaskAssessmentRunMessage.replication_task_assessment_run_arn required"
        )
    return out
