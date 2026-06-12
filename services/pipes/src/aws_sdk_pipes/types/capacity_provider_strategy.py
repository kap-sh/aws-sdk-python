"""Generated from Smithy shape ``com.amazonaws.pipes#CapacityProviderStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.capacity_provider_strategy_item

CapacityProviderStrategy: TypeAlias = list[
    "aws_sdk_pipes.types.capacity_provider_strategy_item.CapacityProviderStrategyItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderStrategy) -> list:
    import aws_sdk_pipes.types.capacity_provider_strategy_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pipes.types.capacity_provider_strategy_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CapacityProviderStrategy:
    import aws_sdk_pipes.types.capacity_provider_strategy_item

    out: CapacityProviderStrategy = []
    for item in data:
        out.append(
            aws_sdk_pipes.types.capacity_provider_strategy_item.deserialize_json(item)
        )
    return out
