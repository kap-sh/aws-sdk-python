"""Generated from Smithy shape ``com.amazonaws.iot#Environments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.environment

Environments: TypeAlias = list["capo_iot.types.environment.Environment"]


# --- restJson1 ser/de ---
def serialize_json(value: Environments) -> list:
    return list(value)


def deserialize_json(data: list) -> Environments:
    return list(data)
