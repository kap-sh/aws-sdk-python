"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationCodeGenerationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_code_generation_job_details

NetworkMigrationCodeGenerationsList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_code_generation_job_details.NetworkMigrationCodeGenerationJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationCodeGenerationsList) -> list:
    import aws_sdk_mgn.types.network_migration_code_generation_job_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_job_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationCodeGenerationsList:
    import aws_sdk_mgn.types.network_migration_code_generation_job_details

    out: NetworkMigrationCodeGenerationsList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_code_generation_job_details.deserialize_json(
                item
            )
        )
    return out
