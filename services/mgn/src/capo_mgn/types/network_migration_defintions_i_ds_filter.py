"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDefintionsIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_definition_id

NetworkMigrationDefintionsIDsFilter: TypeAlias = list[
    "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDefintionsIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> NetworkMigrationDefintionsIDsFilter:
    return list(data)
