"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Conditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.condition

Conditions: TypeAlias = list["capo_observabilityadmin.types.condition.Condition"]


# --- restJson1 ser/de ---
def serialize_json(value: Conditions) -> list:
    import capo_observabilityadmin.types.condition

    out: list = []
    for item in value:
        out.append(capo_observabilityadmin.types.condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Conditions:
    import capo_observabilityadmin.types.condition

    out: Conditions = []
    for item in data:
        out.append(capo_observabilityadmin.types.condition.deserialize_json(item))
    return out
