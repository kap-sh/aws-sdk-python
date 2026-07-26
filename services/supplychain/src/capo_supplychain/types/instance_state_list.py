"""Generated from Smithy shape ``com.amazonaws.supplychain#InstanceStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.instance_state

InstanceStateList: TypeAlias = list[
    "capo_supplychain.types.instance_state.InstanceState"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStateList) -> list:
    import capo_supplychain.types.instance_state

    out: list = []
    for item in value:
        out.append(capo_supplychain.types.instance_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceStateList:
    import capo_supplychain.types.instance_state

    out: InstanceStateList = []
    for item in data:
        out.append(capo_supplychain.types.instance_state.deserialize_json(item))
    return out
