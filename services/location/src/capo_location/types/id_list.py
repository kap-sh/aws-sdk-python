"""Generated from Smithy shape ``com.amazonaws.location#IdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.id

IdList: TypeAlias = list["capo_location.types.id.Id"]


# --- restJson1 ser/de ---
def serialize_json(value: IdList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdList:
    return list(data)
