"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetECSServiceRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_recommendations
    import capo_compute_optimizer.types.get_recommendation_errors
    import capo_compute_optimizer.types.next_token


class GetECSServiceRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of Amazon ECS service recommendations. </p>"""
    ecs_service_recommendations: NotRequired[
        "capo_compute_optimizer.types.ecs_service_recommendations.ECSServiceRecommendations"
    ]
    """<p> An array of objects that describe the Amazon ECS service recommendations. </p>"""
    errors: NotRequired[
        "capo_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p> An array of objects that describe errors of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetECSServiceRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "ecs_service_recommendations" in value:
        import capo_compute_optimizer.types.ecs_service_recommendations

        out["ecsServiceRecommendations"] = (
            capo_compute_optimizer.types.ecs_service_recommendations.serialize_aws_json_1_0(
                value["ecs_service_recommendations"]
            )
        )
    if "errors" in value:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetECSServiceRecommendationsResponse:
    out: GetECSServiceRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "ecsServiceRecommendations" in data:
        import capo_compute_optimizer.types.ecs_service_recommendations

        out["ecs_service_recommendations"] = (
            capo_compute_optimizer.types.ecs_service_recommendations.deserialize_aws_json_1_0(
                data["ecsServiceRecommendations"]
            )
        )
    if "errors" in data:
        import capo_compute_optimizer.types.get_recommendation_errors

        out["errors"] = (
            capo_compute_optimizer.types.get_recommendation_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
