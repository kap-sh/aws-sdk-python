"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationFailedResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_failed_resource_details

NetworkMigrationFailedResourcesList: TypeAlias = list[
    "capo_mgn.types.network_migration_failed_resource_details.NetworkMigrationFailedResourceDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationFailedResourcesList) -> list:
    import capo_mgn.types.network_migration_failed_resource_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_failed_resource_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationFailedResourcesList:
    import capo_mgn.types.network_migration_failed_resource_details

    out: NetworkMigrationFailedResourcesList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_failed_resource_details.deserialize_json(
                item
            )
        )
    return out
