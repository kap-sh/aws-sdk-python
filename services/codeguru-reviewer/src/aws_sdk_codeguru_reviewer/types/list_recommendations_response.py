"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.next_token
    import aws_sdk_codeguru_reviewer.types.recommendation_summaries


class ListRecommendationsResponse(TypedDict, closed=True):
    recommendation_summaries: NotRequired[
        "aws_sdk_codeguru_reviewer.types.recommendation_summaries.RecommendationSummaries"
    ]
    """<p>List of recommendations for the requested code review.</p>"""
    next_token: NotRequired["aws_sdk_codeguru_reviewer.types.next_token.NextToken"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "recommendation_summaries" in value:
        import aws_sdk_codeguru_reviewer.types.recommendation_summaries

        out["RecommendationSummaries"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_summaries.serialize_json(
                value["recommendation_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "RecommendationSummaries" in data:
        import aws_sdk_codeguru_reviewer.types.recommendation_summaries

        out["recommendation_summaries"] = (
            aws_sdk_codeguru_reviewer.types.recommendation_summaries.deserialize_json(
                data["RecommendationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
