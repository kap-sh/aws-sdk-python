"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IntegerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer

IntegerList: TypeAlias = list["capo_database_migration_service.types.integer.Integer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IntegerList:
    return list(data)
