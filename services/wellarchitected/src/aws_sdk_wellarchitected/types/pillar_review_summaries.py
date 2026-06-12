"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PillarReviewSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.pillar_review_summary

PillarReviewSummaries: TypeAlias = list[
    "aws_sdk_wellarchitected.types.pillar_review_summary.PillarReviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PillarReviewSummaries) -> list:
    import aws_sdk_wellarchitected.types.pillar_review_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.pillar_review_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PillarReviewSummaries:
    import aws_sdk_wellarchitected.types.pillar_review_summary

    out: PillarReviewSummaries = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.pillar_review_summary.deserialize_json(item)
        )
    return out
