"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__integerMin32Max8182``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min32_max8182

__listOf__integerMin32Max8182: TypeAlias = list[
    "capo_mediaconvert.types.__integer_min32_max8182.__integerMin32Max8182"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__integerMin32Max8182) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__integerMin32Max8182:
    return list(data)
