"""Generated from Smithy shape ``com.amazonaws.medialive#__listOf__stringPatternS``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.__string_pattern_s

__listOf__stringPatternS: TypeAlias = list[
    "capo_medialive.types.__string_pattern_s.__stringPatternS"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringPatternS) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringPatternS:
    return list(data)
