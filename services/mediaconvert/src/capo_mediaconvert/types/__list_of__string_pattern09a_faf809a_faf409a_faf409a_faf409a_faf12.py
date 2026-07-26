"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12

__listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12: TypeAlias = list[
    "capo_mediaconvert.types.__string_pattern09a_faf809a_faf409a_faf409a_faf409a_faf12.__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: __listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12,
) -> list:
    return list(value)


def deserialize_json(
    data: list,
) -> __listOf__stringPattern09aFAF809aFAF409aFAF409aFAF409aFAF12:
    return list(data)
