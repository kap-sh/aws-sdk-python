"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_code_generation_job_details

NetworkMigrationCodeGenerationsList: TypeAlias = list[
    "capo_mgn.types.network_migration_code_generation_job_details.NetworkMigrationCodeGenerationJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationsList) -> list:
    import capo_mgn.types.network_migration_code_generation_job_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_code_generation_job_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationsList:
    import capo_mgn.types.network_migration_code_generation_job_details

    out: NetworkMigrationCodeGenerationsList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_code_generation_job_details.deserialize_json(
                item
            )
        )
    return out
