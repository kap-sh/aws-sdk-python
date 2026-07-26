"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationAnalysesIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_job_id

ListNetworkMigrationAnalysesIDsFilter: TypeAlias = list[
    "capo_mgn.types.network_migration_job_id.NetworkMigrationJobID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationAnalysesIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationAnalysesIDsFilter:
    return list(data)
