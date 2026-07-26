"""Generated from Smithy shape ``com.amazonaws.outposts#EC2FamilyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.family

EC2FamilyList: TypeAlias = list["capo_outposts.types.family.Family"]


# --- restJson1 ser/de ---
def serialize_json(value: EC2FamilyList) -> list:
    return list(value)


def deserialize_json(data: list) -> EC2FamilyList:
    return list(data)
