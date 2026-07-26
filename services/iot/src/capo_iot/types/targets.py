"""Generated from Smithy shape ``com.amazonaws.iot#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.target

Targets: TypeAlias = list["capo_iot.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: Targets) -> list:
    return list(value)


def deserialize_json(data: list) -> Targets:
    return list(data)
