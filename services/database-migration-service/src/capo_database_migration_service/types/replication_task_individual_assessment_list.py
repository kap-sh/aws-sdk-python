"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationTaskIndividualAssessmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.replication_task_individual_assessment

ReplicationTaskIndividualAssessmentList: TypeAlias = list[
    "capo_database_migration_service.types.replication_task_individual_assessment.ReplicationTaskIndividualAssessment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationTaskIndividualAssessmentList) -> list:
    import capo_database_migration_service.types.replication_task_individual_assessment

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.replication_task_individual_assessment.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationTaskIndividualAssessmentList:
    import capo_database_migration_service.types.replication_task_individual_assessment

    out: ReplicationTaskIndividualAssessmentList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.replication_task_individual_assessment.deserialize_aws_json_1_1(
                item
            )
        )
    return out
