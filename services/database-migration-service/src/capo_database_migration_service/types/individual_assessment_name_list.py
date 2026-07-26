"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IndividualAssessmentNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.string

IndividualAssessmentNameList: TypeAlias = list[
    "capo_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndividualAssessmentNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IndividualAssessmentNameList:
    return list(data)
