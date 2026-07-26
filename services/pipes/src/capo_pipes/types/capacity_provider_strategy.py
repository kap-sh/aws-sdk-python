"""Generated from Smithy shape ``com.amazonaws.pipes#CapacityProviderStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.capacity_provider_strategy_item

CapacityProviderStrategy: TypeAlias = list[
    "capo_pipes.types.capacity_provider_strategy_item.CapacityProviderStrategyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderStrategy) -> list:
    import capo_pipes.types.capacity_provider_strategy_item

    out: list = []
    for item in value:
        out.append(
            capo_pipes.types.capacity_provider_strategy_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapacityProviderStrategy:
    import capo_pipes.types.capacity_provider_strategy_item

    out: CapacityProviderStrategy = []
    for item in data:
        out.append(
            capo_pipes.types.capacity_provider_strategy_item.deserialize_json(item)
        )
    return out
