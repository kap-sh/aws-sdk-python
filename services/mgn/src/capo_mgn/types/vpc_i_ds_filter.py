"""Generated from Smithy shape ``com.amazonaws.mgn#VpcIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.vpc_id

VpcIDsFilter: TypeAlias = list["capo_mgn.types.vpc_id.VpcID"]


# --- restJson1 ser/de ---
def serialize_json(value: VpcIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> VpcIDsFilter:
    return list(data)
