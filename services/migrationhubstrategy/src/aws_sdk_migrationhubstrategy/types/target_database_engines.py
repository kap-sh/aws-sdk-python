"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#TargetDatabaseEngines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.target_database_engine

TargetDatabaseEngines: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.target_database_engine.TargetDatabaseEngine"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDatabaseEngines) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetDatabaseEngines:
    return list(data)
