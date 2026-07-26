"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDeployedStacksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_deployed_stack_details

NetworkMigrationDeployedStacksList: TypeAlias = list[
    "capo_mgn.types.network_migration_deployed_stack_details.NetworkMigrationDeployedStackDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDeployedStacksList) -> list:
    import capo_mgn.types.network_migration_deployed_stack_details

    out: list = []
    for item in value:
        out.append(
            capo_mgn.types.network_migration_deployed_stack_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationDeployedStacksList:
    import capo_mgn.types.network_migration_deployed_stack_details

    out: NetworkMigrationDeployedStacksList = []
    for item in data:
        out.append(
            capo_mgn.types.network_migration_deployed_stack_details.deserialize_json(
                item
            )
        )
    return out
