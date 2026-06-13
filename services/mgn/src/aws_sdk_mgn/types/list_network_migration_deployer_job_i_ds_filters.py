"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationDeployerJobIDsFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_job_id

ListNetworkMigrationDeployerJobIDsFilters: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_job_id.NetworkMigrationJobID"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationDeployerJobIDsFilters) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationDeployerJobIDsFilters:
    return list(data)
