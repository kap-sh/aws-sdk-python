"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#EnvironmentVpcs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_vpc

EnvironmentVpcs: TypeAlias = list[
    "capo_migration_hub_refactor_spaces.types.environment_vpc.EnvironmentVpc"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentVpcs) -> list:
    import capo_migration_hub_refactor_spaces.types.environment_vpc

    out: list = []
    for item in value:
        out.append(
            capo_migration_hub_refactor_spaces.types.environment_vpc.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentVpcs:
    import capo_migration_hub_refactor_spaces.types.environment_vpc

    out: EnvironmentVpcs = []
    for item in data:
        out.append(
            capo_migration_hub_refactor_spaces.types.environment_vpc.deserialize_json(
                item
            )
        )
    return out
