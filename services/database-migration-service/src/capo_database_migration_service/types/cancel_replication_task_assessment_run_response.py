"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CancelReplicationTaskAssessmentRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task_assessment_run


class CancelReplicationTaskAssessmentRunResponse(TypedDict, closed=True):
    replication_task_assessment_run: NotRequired[
        "capo_database_migration_service.types.replication_task_assessment_run.ReplicationTaskAssessmentRun"
    ]
    """<p>The <code>ReplicationTaskAssessmentRun</code> object for the canceled assessment run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelReplicationTaskAssessmentRunResponse) -> dict:
    out: dict = {}
    if "replication_task_assessment_run" in value:
        import capo_database_migration_service.types.replication_task_assessment_run

        out["ReplicationTaskAssessmentRun"] = (
            capo_database_migration_service.types.replication_task_assessment_run.serialize_aws_json_1_1(
                value["replication_task_assessment_run"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelReplicationTaskAssessmentRunResponse:
    out: CancelReplicationTaskAssessmentRunResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskAssessmentRun" in data:
        import capo_database_migration_service.types.replication_task_assessment_run

        out["replication_task_assessment_run"] = (
            capo_database_migration_service.types.replication_task_assessment_run.deserialize_aws_json_1_1(
                data["ReplicationTaskAssessmentRun"]
            )
        )
    return out
