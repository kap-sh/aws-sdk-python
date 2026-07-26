"""Generated from Smithy shape ``com.amazonaws.supplychain#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.instance

InstanceList: TypeAlias = list["capo_supplychain.types.instance.Instance"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceList) -> list:
    import capo_supplychain.types.instance

    out: list = []
    for item in value:
        out.append(capo_supplychain.types.instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceList:
    import capo_supplychain.types.instance

    out: InstanceList = []
    for item in data:
        out.append(capo_supplychain.types.instance.deserialize_json(item))
    return out
