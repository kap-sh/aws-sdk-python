"""Generated from Smithy shape ``com.amazonaws.novaact#Calls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.call

Calls: TypeAlias = list["capo_nova_act.types.call.Call"]


# --- restJson1 ser/de ---
def serialize_json(value: Calls) -> list:
    import capo_nova_act.types.call

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.call.serialize_json(item))
    return out


def deserialize_json(data: list) -> Calls:
    import capo_nova_act.types.call

    out: Calls = []
    for item in data:
        out.append(capo_nova_act.types.call.deserialize_json(item))
    return out
