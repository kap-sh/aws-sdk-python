"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CompositionRelationshipSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.composition_relationship_summary

CompositionRelationshipSummaries: TypeAlias = list[
    "capo_iotsitewise.types.composition_relationship_summary.CompositionRelationshipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionRelationshipSummaries) -> list:
    import capo_iotsitewise.types.composition_relationship_summary

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.composition_relationship_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CompositionRelationshipSummaries:
    import capo_iotsitewise.types.composition_relationship_summary

    out: CompositionRelationshipSummaries = []
    for item in data:
        out.append(
            capo_iotsitewise.types.composition_relationship_summary.deserialize_json(
                item
            )
        )
    return out
