"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_trustedadvisor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation_summary_list


class ListRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    recommendation_summaries: "aws_sdk_trustedadvisor.types.recommendation_summary_list.RecommendationSummaryList"
    """<p>The list of Recommendations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_trustedadvisor.types.recommendation_summary_list

    out["recommendationSummaries"] = (
        aws_sdk_trustedadvisor.types.recommendation_summary_list.serialize_json(
            value["recommendation_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recommendationSummaries" in data:
        import aws_sdk_trustedadvisor.types.recommendation_summary_list

        out["recommendation_summaries"] = (
            aws_sdk_trustedadvisor.types.recommendation_summary_list.deserialize_json(
                data["recommendationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListRecommendationsResponse.recommendation_summaries required"
        )
    return out
