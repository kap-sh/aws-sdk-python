"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensReviewSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.lens_review_summary

LensReviewSummaries: TypeAlias = list[
    "capo_wellarchitected.types.lens_review_summary.LensReviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LensReviewSummaries) -> list:
    import capo_wellarchitected.types.lens_review_summary

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.lens_review_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LensReviewSummaries:
    import capo_wellarchitected.types.lens_review_summary

    out: LensReviewSummaries = []
    for item in data:
        out.append(
            capo_wellarchitected.types.lens_review_summary.deserialize_json(item)
        )
    return out
