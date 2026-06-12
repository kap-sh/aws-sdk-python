"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelReplicationTaskAssessmentRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run


class CancelReplicationTaskAssessmentRunResponse(TypedDict):
    replication_task_assessment_run: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task_assessment_run.ReplicationTaskAssessmentRun"
    ]
    """<p>The <code>ReplicationTaskAssessmentRun</code> object for the canceled assessment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplicationTaskAssessmentRunResponse) -> dict:
    out: dict = {}
    if "replication_task_assessment_run" in value:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run

        out["ReplicationTaskAssessmentRun"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run.serialize_aws_json_1_1(
                value["replication_task_assessment_run"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplicationTaskAssessmentRunResponse:
    out: CancelReplicationTaskAssessmentRunResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskAssessmentRun" in data:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run

        out["replication_task_assessment_run"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentRun"]
            )
        )
    return out
