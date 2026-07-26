"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#HeterogeneousTargetDatabaseEngines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.heterogeneous_target_database_engine

HeterogeneousTargetDatabaseEngines: TypeAlias = list[
    "capo_migrationhubstrategy.types.heterogeneous_target_database_engine.HeterogeneousTargetDatabaseEngine"
]


# --- restJson1 ser/de ---
def serialize_json(value: HeterogeneousTargetDatabaseEngines) -> list:
    return list(value)


def deserialize_json(data: list) -> HeterogeneousTargetDatabaseEngines:
    return list(data)
