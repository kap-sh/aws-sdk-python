"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationExecutionStatusesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.execution_status

NetworkMigrationExecutionStatusesFilter: TypeAlias = list[
    "capo_mgn.types.execution_status.ExecutionStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationExecutionStatusesFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkMigrationExecutionStatusesFilter:
    return list(data)
