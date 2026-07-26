"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SuggestedChangesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.entity_description

SuggestedChangesList: TypeAlias = list[
    "capo_resiliencehubv2.types.entity_description.EntityDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedChangesList) -> list:
    return list(value)


def deserialize_json(data: list) -> SuggestedChangesList:
    return list(data)
