"""Generated from Smithy shape ``com.amazonaws.iot#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.resource

Resources: TypeAlias = list["capo_iot.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    return list(value)


def deserialize_json(data: list) -> Resources:
    return list(data)
