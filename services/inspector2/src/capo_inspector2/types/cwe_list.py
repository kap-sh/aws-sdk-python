"""Generated from Smithy shape ``com.amazonaws.inspector2#CweList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string

CweList: TypeAlias = list["capo_inspector2.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: CweList) -> list:
    return list(value)


def deserialize_json(data: list) -> CweList:
    return list(data)
