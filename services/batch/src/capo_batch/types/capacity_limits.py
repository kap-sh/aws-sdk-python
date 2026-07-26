"""Generated from Smithy shape ``com.amazonaws.batch#CapacityLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.capacity_limit

CapacityLimits: TypeAlias = list["capo_batch.types.capacity_limit.CapacityLimit"]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityLimits) -> list:
    import capo_batch.types.capacity_limit

    out: list = []
    for item in value:
        out.append(capo_batch.types.capacity_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityLimits:
    import capo_batch.types.capacity_limit

    out: CapacityLimits = []
    for item in data:
        out.append(capo_batch.types.capacity_limit.deserialize_json(item))
    return out
