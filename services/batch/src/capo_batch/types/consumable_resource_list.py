"""Generated from Smithy shape ``com.amazonaws.batch#ConsumableResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.consumable_resource_requirement

ConsumableResourceList: TypeAlias = list[
    "capo_batch.types.consumable_resource_requirement.ConsumableResourceRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsumableResourceList) -> list:
    import capo_batch.types.consumable_resource_requirement

    out: list = []
    for item in value:
        out.append(
            capo_batch.types.consumable_resource_requirement.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConsumableResourceList:
    import capo_batch.types.consumable_resource_requirement

    out: ConsumableResourceList = []
    for item in data:
        out.append(
            capo_batch.types.consumable_resource_requirement.deserialize_json(item)
        )
    return out
