"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PremigrationAssessmentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.premigration_assessment_status

PremigrationAssessmentStatusList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.premigration_assessment_status.PremigrationAssessmentStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PremigrationAssessmentStatusList) -> list:
    import aws_sdk_database_migration_service.types.premigration_assessment_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.premigration_assessment_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PremigrationAssessmentStatusList:
    import aws_sdk_database_migration_service.types.premigration_assessment_status

    out: PremigrationAssessmentStatusList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.premigration_assessment_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
