"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationSummariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.recommendation_summaries


class GetRecommendationSummariesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of recommendation summaries.</p> <p>This value is null when there are no more pages of recommendation summaries to return.</p>"""
    recommendation_summaries: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_summaries.RecommendationSummaries"
    ]
    """<p>An array of objects that summarize a recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationSummariesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_summaries" in value:
        import aws_sdk_compute_optimizer.types.recommendation_summaries

        out["recommendationSummaries"] = (
            aws_sdk_compute_optimizer.types.recommendation_summaries.serialize_aws_json_1_0(
                value["recommendation_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationSummariesResponse:
    out: GetRecommendationSummariesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recommendationSummaries" in data:
        import aws_sdk_compute_optimizer.types.recommendation_summaries

        out["recommendation_summaries"] = (
            aws_sdk_compute_optimizer.types.recommendation_summaries.deserialize_aws_json_1_0(
                data["recommendationSummaries"]
            )
        )
    return out
