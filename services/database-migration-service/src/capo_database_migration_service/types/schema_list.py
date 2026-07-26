"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.string

SchemaList: TypeAlias = list["capo_database_migration_service.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SchemaList:
    return list(data)
