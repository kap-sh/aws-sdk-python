"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SubnetIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string

SubnetIdentifierList: TypeAlias = list[
    "aws_sdk_database_migration_service.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIdentifierList:
    return list(data)
