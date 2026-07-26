"""Generated from Smithy shape ``com.amazonaws.scheduler#PlacementStrategies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.placement_strategy

PlacementStrategies: TypeAlias = list[
    "capo_scheduler.types.placement_strategy.PlacementStrategy"
]


# --- restJson1 ser/de ---
def serialize_json(value: PlacementStrategies) -> list:
    import capo_scheduler.types.placement_strategy

    out: list = []
    for item in value:
        out.append(capo_scheduler.types.placement_strategy.serialize_json(item))
    return out


def deserialize_json(data: list) -> PlacementStrategies:
    import capo_scheduler.types.placement_strategy

    out: PlacementStrategies = []
    for item in data:
        out.append(capo_scheduler.types.placement_strategy.deserialize_json(item))
    return out
