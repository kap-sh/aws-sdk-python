"""Generated from Smithy shape ``com.amazonaws.eventbridge#CapacityProviderStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.capacity_provider_strategy_item

CapacityProviderStrategy: TypeAlias = list[
    "capo_eventbridge.types.capacity_provider_strategy_item.CapacityProviderStrategyItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderStrategy) -> list:
    import capo_eventbridge.types.capacity_provider_strategy_item

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.capacity_provider_strategy_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CapacityProviderStrategy:
    import capo_eventbridge.types.capacity_provider_strategy_item

    out: CapacityProviderStrategy = []
    for item in data:
        out.append(
            capo_eventbridge.types.capacity_provider_strategy_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
