"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__integerMin1Max2147483647``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__integer_min1_max2147483647

__listOf__integerMin1Max2147483647: TypeAlias = list[
    "capo_mediaconvert.types.__integer_min1_max2147483647.__integerMin1Max2147483647"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__integerMin1Max2147483647) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__integerMin1Max2147483647:
    return list(data)
