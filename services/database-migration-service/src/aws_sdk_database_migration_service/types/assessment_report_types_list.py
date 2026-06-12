"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AssessmentReportTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.assessment_report_type

AssessmentReportTypesList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.assessment_report_type.AssessmentReportType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentReportTypesList) -> list:
    import aws_sdk_database_migration_service.types.assessment_report_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.assessment_report_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentReportTypesList:
    import aws_sdk_database_migration_service.types.assessment_report_type

    out: AssessmentReportTypesList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.assessment_report_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
