"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationDeployedStacksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.network_migration_deployed_stack_details

NetworkMigrationDeployedStacksList: TypeAlias = list[
    "aws_sdk_mgn.types.network_migration_deployed_stack_details.NetworkMigrationDeployedStackDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationDeployedStacksList) -> list:
    import aws_sdk_mgn.types.network_migration_deployed_stack_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mgn.types.network_migration_deployed_stack_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NetworkMigrationDeployedStacksList:
    import aws_sdk_mgn.types.network_migration_deployed_stack_details

    out: NetworkMigrationDeployedStacksList = []
    for item in data:
        out.append(
            aws_sdk_mgn.types.network_migration_deployed_stack_details.deserialize_json(
                item
            )
        )
    return out
