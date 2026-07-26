"""Generated from Smithy shape ``com.amazonaws.medialive#__listOf__stringMin7Max11PatternAws097``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.__string_min7_max11_pattern_aws097

__listOf__stringMin7Max11PatternAws097: TypeAlias = list[
    "capo_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMin7Max11PatternAws097) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMin7Max11PatternAws097:
    return list(data)
