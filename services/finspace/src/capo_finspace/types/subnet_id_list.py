"""Generated from Smithy shape ``com.amazonaws.finspace#SubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.subnet_id_string

SubnetIdList: TypeAlias = list["capo_finspace.types.subnet_id_string.SubnetIdString"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIdList:
    return list(data)
