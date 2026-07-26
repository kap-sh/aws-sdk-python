"""Generated from Smithy shape ``com.amazonaws.chime#UserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string

UserIdList: TypeAlias = list["capo_chime.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: UserIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserIdList:
    return list(data)
