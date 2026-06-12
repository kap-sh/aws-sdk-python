"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLicenseRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.get_recommendation_errors
    import aws_sdk_compute_optimizer.types.license_recommendations
    import aws_sdk_compute_optimizer.types.next_token


class GetLicenseRecommendationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p> The token to use to advance to the next page of license recommendations. </p>"""
    license_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.license_recommendations.LicenseRecommendations"
    ]
    """<p> An array of objects that describe license recommendations. </p>"""
    errors: NotRequired[
        "aws_sdk_compute_optimizer.types.get_recommendation_errors.GetRecommendationErrors"
    ]
    """<p> An array of objects that describe errors of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLicenseRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "license_recommendations" in value:
        import aws_sdk_compute_optimizer.types.license_recommendations

        out["licenseRecommendations"] = (
            aws_sdk_compute_optimizer.types.license_recommendations.serialize_aws_json_1_0(
                value["license_recommendations"]
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


def deserialize_aws_json_1_0(data: dict) -> GetLicenseRecommendationsResponse:
    out: GetLicenseRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "licenseRecommendations" in data:
        import aws_sdk_compute_optimizer.types.license_recommendations

        out["license_recommendations"] = (
            aws_sdk_compute_optimizer.types.license_recommendations.deserialize_aws_json_1_0(
                data["licenseRecommendations"]
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
