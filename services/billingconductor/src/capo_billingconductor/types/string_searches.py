"""Generated from Smithy shape ``com.amazonaws.billingconductor#StringSearches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.string_search

StringSearches: TypeAlias = list[
    "capo_billingconductor.types.string_search.StringSearch"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringSearches) -> list:
    import capo_billingconductor.types.string_search

    out: list = []
    for item in value:
        out.append(capo_billingconductor.types.string_search.serialize_json(item))
    return out


def deserialize_json(data: list) -> StringSearches:
    import capo_billingconductor.types.string_search

    out: StringSearches = []
    for item in data:
        out.append(capo_billingconductor.types.string_search.deserialize_json(item))
    return out
