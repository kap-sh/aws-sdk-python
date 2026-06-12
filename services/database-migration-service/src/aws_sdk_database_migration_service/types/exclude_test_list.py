"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExcludeTestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string

ExcludeTestList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeTestList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeTestList:
    return list(data)
