"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.space_quick_sight_resource

SpaceQuickSightResources: TypeAlias = list[
    "capo_quicksight.types.space_quick_sight_resource.SpaceQuickSightResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightResources) -> list:
    import capo_quicksight.types.space_quick_sight_resource

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.space_quick_sight_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SpaceQuickSightResources:
    import capo_quicksight.types.space_quick_sight_resource

    out: SpaceQuickSightResources = []
    for item in data:
        out.append(
            capo_quicksight.types.space_quick_sight_resource.deserialize_json(item)
        )
    return out
