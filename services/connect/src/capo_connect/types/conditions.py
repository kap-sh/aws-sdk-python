"""Generated from Smithy shape ``com.amazonaws.connect#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.condition

Conditions: TypeAlias = list["capo_connect.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> list:
    import capo_connect.types.condition

    out: list = []
    for item in value:
        out.append(capo_connect.types.condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Conditions:
    import capo_connect.types.condition

    out: Conditions = []
    for item in data:
        out.append(capo_connect.types.condition.deserialize_json(item))
    return out
