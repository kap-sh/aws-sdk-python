"""Generated from Smithy shape ``com.amazonaws.m2#String50List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.string50

String50List: TypeAlias = list["capo_m2.types.string50.String50"]


# --- restJson1 ser/de ---
def serialize_json(value: String50List) -> list:
    return list(value)


def deserialize_json(data: list) -> String50List:
    return list(data)
