"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRDSDatabaseRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.get_recommendation_errors
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.rdsdb_recommendations


class GetRDSDatabaseRecommendationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to advance to the next page of Amazon Aurora and RDS database recommendations. </p>"""
    rds_db_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.rdsdb_recommendations.RDSDBRecommendations"
    ]
    """<p> An array of objects that describe the Amazon Aurora and RDS database recommendations. </p>"""
    errors: NotRequired[
        "aws_sdk_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p> An array of objects that describe errors of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRDSDatabaseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "rds_db_recommendations" in value:
        import aws_sdk_compute_optimizer.types.rdsdb_recommendations

        out["rdsDBRecommendations"] = (
            aws_sdk_compute_optimizer.types.rdsdb_recommendations.serialize_aws_json_1_0(
                value["rds_db_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetRDSDatabaseRecommendationsResponse:
    out: GetRDSDatabaseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "rdsDBRecommendations" in data:
        import aws_sdk_compute_optimizer.types.rdsdb_recommendations

        out["rds_db_recommendations"] = (
            aws_sdk_compute_optimizer.types.rdsdb_recommendations.deserialize_aws_json_1_0(
                data["rdsDBRecommendations"]
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
