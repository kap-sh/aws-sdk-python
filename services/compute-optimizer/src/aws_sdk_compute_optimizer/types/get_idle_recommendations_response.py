"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetIdleRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_recommendation_errors
    import aws_sdk_compute_optimizer.types.idle_recommendations
    import aws_sdk_compute_optimizer.types.next_token


class GetIdleRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of idle resource recommendations.</p>"""
    idle_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_recommendations.IdleRecommendations"
    ]
    """<p>An array of objects that describe the idle resource recommendations.</p>"""
    errors: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_recommendation_errors.IdleRecommendationErrors"
    ]
    """<p>An array of objects that describe errors of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdleRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "idle_recommendations" in value:
        import aws_sdk_compute_optimizer.types.idle_recommendations

        out["idleRecommendations"] = (
            aws_sdk_compute_optimizer.types.idle_recommendations.serialize_aws_json_1_0(
                value["idle_recommendations"]
            )
        )
    if "errors" in value:
        import aws_sdk_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdleRecommendationsResponse:
    out: GetIdleRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "idleRecommendations" in data:
        import aws_sdk_compute_optimizer.types.idle_recommendations

        out["idle_recommendations"] = (
            aws_sdk_compute_optimizer.types.idle_recommendations.deserialize_aws_json_1_0(
                data["idleRecommendations"]
            )
        )
    if "errors" in data:
        import aws_sdk_compute_optimizer.types.idle_recommendation_errors

        out["errors"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
