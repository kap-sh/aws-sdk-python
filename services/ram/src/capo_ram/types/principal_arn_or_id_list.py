"""Generated from Smithy shape ``com.amazonaws.ram#PrincipalArnOrIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.string

PrincipalArnOrIdList: TypeAlias = list["capo_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalArnOrIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrincipalArnOrIdList:
    return list(data)
