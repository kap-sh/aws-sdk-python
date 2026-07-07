"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#StartReplicationTaskAssessmentRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run


class StartReplicationTaskAssessmentRunResponse(TypedDict, closed=True):
    replication_task_assessment_run: NotRequired[
        "aws_sdk_database_migration_service.types.replication_task_assessment_run.ReplicationTaskAssessmentRun"
    ]
    """<p>The premigration assessment run that was started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartReplicationTaskAssessmentRunResponse) -> dict:
    out: dict = {}
    if "replication_task_assessment_run" in value:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run

        out["ReplicationTaskAssessmentRun"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run.serialize_aws_json_1_1(
                value["replication_task_assessment_run"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartReplicationTaskAssessmentRunResponse:
    out: StartReplicationTaskAssessmentRunResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskAssessmentRun" in data:
        import aws_sdk_database_migration_service.types.replication_task_assessment_run

        out["replication_task_assessment_run"] = (
            aws_sdk_database_migration_service.types.replication_task_assessment_run.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentRun"]
            )
        )
    return out
