"""Generated from Smithy shape ``com.amazonaws.novaact#CallResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.call_result

CallResults: TypeAlias = list["capo_nova_act.types.call_result.CallResult"]


# --- restJson1 ser/de ---
def serialize_json(value: CallResults) -> list:
    import capo_nova_act.types.call_result

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.call_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallResults:
    import capo_nova_act.types.call_result

    out: CallResults = []
    for item in data:
        out.append(capo_nova_act.types.call_result.deserialize_json(item))
    return out
