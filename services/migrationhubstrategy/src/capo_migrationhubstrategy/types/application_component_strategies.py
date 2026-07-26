"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_strategy

ApplicationComponentStrategies: TypeAlias = list[
    "capo_migrationhubstrategy.types.application_component_strategy.ApplicationComponentStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentStrategies) -> list:
    import capo_migrationhubstrategy.types.application_component_strategy

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.application_component_strategy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ApplicationComponentStrategies:
    import capo_migrationhubstrategy.types.application_component_strategy

    out: ApplicationComponentStrategies = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.application_component_strategy.deserialize_json(
                item
            )
        )
    return out
