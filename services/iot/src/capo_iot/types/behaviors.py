"""Generated from Smithy shape ``com.amazonaws.iot#Behaviors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.behavior

Behaviors: TypeAlias = list["capo_iot.types.behavior.Behavior"]


# --- restJson1 ser/de ---
def serialize_json(value: Behaviors) -> list:
    import capo_iot.types.behavior

    out: list = []
    for item in value:
        out.append(capo_iot.types.behavior.serialize_json(item))
    return out


def deserialize_json(data: list) -> Behaviors:
    import capo_iot.types.behavior

    out: Behaviors = []
    for item in data:
        out.append(capo_iot.types.behavior.deserialize_json(item))
    return out
