"""Generated from Smithy shape ``com.amazonaws.datazone#VpcConnectionSubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.subnet_id

VpcConnectionSubnetIdList: TypeAlias = list["capo_datazone.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectionSubnetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> VpcConnectionSubnetIdList:
    return list(data)
