"""Generated from Smithy shape ``com.amazonaws.scheduler#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_scheduler.types.subnet

Subnets: TypeAlias = list["capo_scheduler.types.subnet.Subnet"]


# --- restJson1 ser/de ---
def serialize_json(value: Subnets) -> list:
    return list(value)


def deserialize_json(data: list) -> Subnets:
    return [item for item in data if item is not None]
