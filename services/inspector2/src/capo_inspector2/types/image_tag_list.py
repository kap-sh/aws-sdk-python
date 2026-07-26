"""Generated from Smithy shape ``com.amazonaws.inspector2#ImageTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.non_empty_string

ImageTagList: TypeAlias = list["capo_inspector2.types.non_empty_string.NonEmptyString"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageTagList) -> list:
    return list(value)


def deserialize_json(data: list) -> ImageTagList:
    return list(data)
