"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDeployerJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_deployer_job_details

NetworkMigrationDeployerJobList: TypeAlias = list[
    "capo_mgn.types.network_migration_deployer_job_details.NetworkMigrationDeployerJobDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDeployerJobList) -> list:
    import capo_mgn.types.network_migration_deployer_job_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_deployer_job_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationDeployerJobList:
    import capo_mgn.types.network_migration_deployer_job_details

    out: NetworkMigrationDeployerJobList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_deployer_job_details.deserialize_json(item)
        )
    return out
