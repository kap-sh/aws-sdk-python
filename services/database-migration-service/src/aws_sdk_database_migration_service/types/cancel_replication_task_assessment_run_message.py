"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelReplicationTaskAssessmentRunMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class CancelReplicationTaskAssessmentRunMessage(TypedDict, closed=True):
    replication_task_assessment_run_arn: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>Amazon Resource Name (ARN) of the premigration assessment run to be canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplicationTaskAssessmentRunMessage) -> dict:
    out: dict = {}
    out["ReplicationTaskAssessmentRunArn"] = value[
        "replication_task_assessment_run_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplicationTaskAssessmentRunMessage:
    out: CancelReplicationTaskAssessmentRunMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskAssessmentRunArn" in data:
        out["replication_task_assessment_run_arn"] = data[
            "ReplicationTaskAssessmentRunArn"
        ]
    else:
        raise DeserializationError(
            "CancelReplicationTaskAssessmentRunMessage.replication_task_assessment_run_arn required"
        )
    return out
