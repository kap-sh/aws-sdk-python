"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationProjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.migration_project

MigrationProjectList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.migration_project.MigrationProject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationProjectList) -> list:
    import aws_sdk_database_migration_service.types.migration_project

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.migration_project.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MigrationProjectList:
    import aws_sdk_database_migration_service.types.migration_project

    out: MigrationProjectList = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.migration_project.deserialize_aws_json_1_1(
                item
            )
        )
    return out
