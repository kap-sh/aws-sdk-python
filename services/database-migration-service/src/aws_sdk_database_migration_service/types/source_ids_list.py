"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SourceIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string

SourceIdsList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SourceIdsList:
    return list(data)
