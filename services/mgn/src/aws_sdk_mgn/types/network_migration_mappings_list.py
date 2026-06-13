"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_mapping_job_details

NetworkMigrationMappingsList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_mapping_job_details.NetworkMigrationMappingJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMappingsList) -> list:
    import aws_sdk_mgn.types.network_migration_mapping_job_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_mapping_job_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationMappingsList:
    import aws_sdk_mgn.types.network_migration_mapping_job_details

    out: NetworkMigrationMappingsList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_mapping_job_details.deserialize_json(
                item
            )
        )
    return out
