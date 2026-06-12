"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataMigrations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.data_migration

DataMigrations: TypeAlias = list[
    "aws_sdk_database_migration_service.types.data_migration.DataMigration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataMigrations) -> list:
    import aws_sdk_database_migration_service.types.data_migration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_database_migration_service.types.data_migration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataMigrations:
    import aws_sdk_database_migration_service.types.data_migration

    out: DataMigrations = []
    for item in data:
        out.append(
            aws_sdk_database_migration_service.types.data_migration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
