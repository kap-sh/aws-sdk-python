"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMappingUpdatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_mapping_update_job_details

NetworkMigrationMappingUpdatesList: TypeAlias = list[
    "capo_mgn.types.network_migration_mapping_update_job_details.NetworkMigrationMappingUpdateJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMappingUpdatesList) -> list:
    import capo_mgn.types.network_migration_mapping_update_job_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_mapping_update_job_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationMappingUpdatesList:
    import capo_mgn.types.network_migration_mapping_update_job_details

    out: NetworkMigrationMappingUpdatesList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_mapping_update_job_details.deserialize_json(
                item
            )
        )
    return out
