"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEBSVolumeRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.get_recommendation_errors
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.volume_recommendations


class GetEBSVolumeRecommendationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of volume recommendations.</p> <p>This value is null when there are no more pages of volume recommendations to return.</p>"""
    volume_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.volume_recommendations.VolumeRecommendations"
    ]
    """<p>An array of objects that describe volume recommendations.</p>"""
    errors: NotRequired[
        "aws_sdk_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p> <p>For example, an error is returned if you request recommendations for an unsupported volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEBSVolumeRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "volume_recommendations" in value:
        import aws_sdk_compute_optimizer.types.volume_recommendations

        out["volumeRecommendations"] = (
            aws_sdk_compute_optimizer.types.volume_recommendations.serialize_aws_json_1_0(
                value["volume_recommendations"]
            )
        )
    if "errors" in value:
        import aws_sdk_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            aws_sdk_compute_optimizer.types.get_recommendation_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEBSVolumeRecommendationsResponse:
    out: GetEBSVolumeRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "volumeRecommendations" in data:
        import aws_sdk_compute_optimizer.types.volume_recommendations

        out["volume_recommendations"] = (
            aws_sdk_compute_optimizer.types.volume_recommendations.deserialize_aws_json_1_0(
                data["volumeRecommendations"]
            )
        )
    if "errors" in data:
        import aws_sdk_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            aws_sdk_compute_optimizer.types.get_recommendation_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
