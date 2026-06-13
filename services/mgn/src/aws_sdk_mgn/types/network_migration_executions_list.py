"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_execution

NetworkMigrationExecutionsList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_execution.NetworkMigrationExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationExecutionsList) -> list:
    import aws_sdk_mgn.types.network_migration_execution

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.network_migration_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkMigrationExecutionsList:
    import aws_sdk_mgn.types.network_migration_execution

    out: NetworkMigrationExecutionsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.network_migration_execution.deserialize_json(item))
    return out
