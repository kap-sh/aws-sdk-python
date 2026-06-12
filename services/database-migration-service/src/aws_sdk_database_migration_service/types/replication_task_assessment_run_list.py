"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskAssessmentRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run

ReplicationTaskAssessmentRunList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.replication_task_assessment_run.ReplicationTaskAssessmentRun"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskAssessmentRunList) -> list:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.replication_task_assessment_run.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationTaskAssessmentRunList:
    import aws_sdk_database_migration_service.types.replication_task_assessment_run

    out: ReplicationTaskAssessmentRunList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.replication_task_assessment_run.deserialize_aws_json_1_1(
                item
            )
        )
    return out
