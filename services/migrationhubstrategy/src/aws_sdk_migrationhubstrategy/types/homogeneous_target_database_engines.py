"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#HomogeneousTargetDatabaseEngines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.homogeneous_target_database_engine

HomogeneousTargetDatabaseEngines: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.homogeneous_target_database_engine.HomogeneousTargetDatabaseEngine"
]


# --- restJson1 ser/de ---
def serialize_json(value: HomogeneousTargetDatabaseEngines) -> list:
    return list(value)


def deserialize_json(data: list) -> HomogeneousTargetDatabaseEngines:
    return list(data)
