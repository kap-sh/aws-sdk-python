"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMappingUpdatesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapping_update_job_details

NetworkMigrationMappingUpdatesList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_mapping_update_job_details.NetworkMigrationMappingUpdateJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMappingUpdatesList) -> list:
    import aws_sdk_mgn.types.network_migration_mapping_update_job_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_mapping_update_job_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationMappingUpdatesList:
    import aws_sdk_mgn.types.network_migration_mapping_update_job_details

    out: NetworkMigrationMappingUpdatesList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_mapping_update_job_details.deserialize_json(
                item
            )
        )
    return out
