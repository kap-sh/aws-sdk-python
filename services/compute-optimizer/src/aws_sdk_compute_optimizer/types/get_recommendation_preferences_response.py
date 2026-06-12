"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationPreferencesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.recommendation_preferences_details


class GetRecommendationPreferencesResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of recommendation preferences.</p> <p>This value is null when there are no more pages of recommendation preferences to return.</p>"""
    recommendation_preferences_details: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_preferences_details.RecommendationPreferencesDetails"
    ]
    """<p>An array of objects that describe recommendation preferences.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationPreferencesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendation_preferences_details" in value:
        import aws_sdk_compute_optimizer.types.recommendation_preferences_details

        out["recommendationPreferencesDetails"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences_details.serialize_aws_json_1_0(
                value["recommendation_preferences_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationPreferencesResponse:
    out: GetRecommendationPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recommendationPreferencesDetails" in data:
        import aws_sdk_compute_optimizer.types.recommendation_preferences_details

        out["recommendation_preferences_details"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences_details.deserialize_aws_json_1_0(
                data["recommendationPreferencesDetails"]
            )
        )
    return out
