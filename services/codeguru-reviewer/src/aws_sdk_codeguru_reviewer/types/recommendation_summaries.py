"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.recommendation_summary

RecommendationSummaries: TypeAlias = list[
    "aws_sdk_codeguru_reviewer.types.recommendation_summary.RecommendationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSummaries) -> list:
    import aws_sdk_codeguru_reviewer.types.recommendation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_reviewer.types.recommendation_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RecommendationSummaries:
    import aws_sdk_codeguru_reviewer.types.recommendation_summary

    out: RecommendationSummaries = []
    for item in data:
        out.append(
            aws_sdk_codeguru_reviewer.types.recommendation_summary.deserialize_json(
                item
            )
        )
    return out
