"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#EntitySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_summary

EntitySummaries: TypeAlias = list[
    "capo_iottwinmaker.types.entity_summary.EntitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EntitySummaries) -> list:
    import capo_iottwinmaker.types.entity_summary

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.entity_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntitySummaries:
    import capo_iottwinmaker.types.entity_summary

    out: EntitySummaries = []
    for item in data:
        out.append(capo_iottwinmaker.types.entity_summary.deserialize_json(item))
    return out
