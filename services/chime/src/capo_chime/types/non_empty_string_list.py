"""Generated from Smithy shape ``com.amazonaws.chime#NonEmptyStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.string

NonEmptyStringList: TypeAlias = list["capo_chime.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: NonEmptyStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> NonEmptyStringList:
    return list(data)
