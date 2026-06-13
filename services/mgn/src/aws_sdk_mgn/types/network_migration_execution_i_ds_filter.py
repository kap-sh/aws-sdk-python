"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationExecutionIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_execution_id

NetworkMigrationExecutionIDsFilter: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationExecutionIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkMigrationExecutionIDsFilter:
    return list(data)
