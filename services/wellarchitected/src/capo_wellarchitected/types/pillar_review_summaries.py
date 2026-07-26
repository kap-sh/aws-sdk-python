"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarReviewSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.pillar_review_summary

PillarReviewSummaries: TypeAlias = list[
    "capo_wellarchitected.types.pillar_review_summary.PillarReviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PillarReviewSummaries) -> list:
    import capo_wellarchitected.types.pillar_review_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.pillar_review_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PillarReviewSummaries:
    import capo_wellarchitected.types.pillar_review_summary

    out: PillarReviewSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.pillar_review_summary.deserialize_json(item)
        )
    return out
