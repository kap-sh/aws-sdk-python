"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMappingUpdatesIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_job_id

ListNetworkMigrationMappingUpdatesIDsFilter: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMappingUpdatesIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationMappingUpdatesIDsFilter:
    return list(data)
