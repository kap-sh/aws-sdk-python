"""Generated from Smithy shape ``com.amazonaws.pipes#CapacityProviderStrategyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.capacity_provider
    import aws_sdk_pipes.types.capacity_provider_strategy_item_base
    import aws_sdk_pipes.types.capacity_provider_strategy_item_weight


class CapacityProviderStrategyItem(TypedDict, closed=True):
    capacity_provider: "aws_sdk_pipes.types.capacity_provider.CapacityProvider"
    """<p>The short name of the capacity provider.</p>"""
    weight: "aws_sdk_pipes.types.capacity_provider_strategy_item_weight.CapacityProviderStrategyItemWeight"
    """<p>The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.</p>"""
    base: "aws_sdk_pipes.types.capacity_provider_strategy_item_base.CapacityProviderStrategyItemBase"
    """<p>The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderStrategyItem) -> dict:
    out: dict = {}
    out["capacityProvider"] = value["capacity_provider"]
    out["weight"] = value.get("weight", 0)
    out["base"] = value.get("base", 0)
    return out


def deserialize_json(data: dict) -> CapacityProviderStrategyItem:
    out: CapacityProviderStrategyItem = {}  # type: ignore[typeddict-item]
    if "capacityProvider" in data:
        out["capacity_provider"] = data["capacityProvider"]
    else:
        raise DeserializationError(
            "CapacityProviderStrategyItem.capacity_provider required"
        )
    if "weight" in data:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if "base" in data:
        out["base"] = data["base"]
    else:
        out["base"] = 0
    return out
