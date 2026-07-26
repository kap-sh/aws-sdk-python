"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MigrationProjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project

MigrationProjectList: TypeAlias = list[
    "capo_database_migration_service.types.migration_project.MigrationProject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationProjectList) -> list:
    import capo_database_migration_service.types.migration_project

    out: list = []
    for item in value:
        out.append(
            capo_database_migration_service.types.migration_project.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MigrationProjectList:
    import capo_database_migration_service.types.migration_project

    out: MigrationProjectList = []
    for item in data:
        out.append(
            capo_database_migration_service.types.migration_project.deserialize_aws_json_1_1(
                item
            )
        )
    return out
