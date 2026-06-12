"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#EnvironmentVpcs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.environment_vpc

EnvironmentVpcs: TypeAlias = list[
    "aws_sdk_migration_hub_refactor_spaces.types.environment_vpc.EnvironmentVpc"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentVpcs) -> list:
    import aws_sdk_migration_hub_refactor_spaces.types.environment_vpc

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub_refactor_spaces.types.environment_vpc.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentVpcs:
    import aws_sdk_migration_hub_refactor_spaces.types.environment_vpc

    out: EnvironmentVpcs = []
    for item in data:
        out.append(
            aws_sdk_migration_hub_refactor_spaces.types.environment_vpc.deserialize_json(
                item
            )
        )
    return out
