"""Generated from Smithy shape ``com.amazonaws.inspector2#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.subnet_id

SubnetIdList: TypeAlias = list["capo_inspector2.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIdList:
    return list(data)
