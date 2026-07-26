"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#HighlightList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string

HighlightList: TypeAlias = list[
    "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: HighlightList) -> list:
    return list(value)


def deserialize_json(data: list) -> HighlightList:
    return list(data)
