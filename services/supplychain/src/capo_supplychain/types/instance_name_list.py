"""Generated from Smithy shape ``com.amazonaws.supplychain#InstanceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supplychain.types.instance_name

InstanceNameList: TypeAlias = list["capo_supplychain.types.instance_name.InstanceName"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceNameList:
    return list(data)
