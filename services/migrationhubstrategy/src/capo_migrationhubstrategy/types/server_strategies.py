"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_strategy

ServerStrategies: TypeAlias = list[
    "capo_migrationhubstrategy.types.server_strategy.ServerStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerStrategies) -> list:
    import capo_migrationhubstrategy.types.server_strategy

    out: list = []
    for item in value:
        out.append(capo_migrationhubstrategy.types.server_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServerStrategies:
    import capo_migrationhubstrategy.types.server_strategy

    out: ServerStrategies = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.server_strategy.deserialize_json(item)
        )
    return out
