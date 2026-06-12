"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLambdaFunctionRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_function_recommendations
    import aws_sdk_compute_optimizer.types.next_token


class GetLambdaFunctionRecommendationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of function recommendations.</p> <p>This value is null when there are no more pages of function recommendations to return.</p>"""
    lambda_function_recommendations: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_function_recommendations.LambdaFunctionRecommendations"
    ]
    """<p>An array of objects that describe function recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLambdaFunctionRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "lambda_function_recommendations" in value:
        import aws_sdk_compute_optimizer.types.lambda_function_recommendations

        out["lambdaFunctionRecommendations"] = (
            aws_sdk_compute_optimizer.types.lambda_function_recommendations.serialize_aws_json_1_0(
                value["lambda_function_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLambdaFunctionRecommendationsResponse:
    out: GetLambdaFunctionRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "lambdaFunctionRecommendations" in data:
        import aws_sdk_compute_optimizer.types.lambda_function_recommendations

        out["lambda_function_recommendations"] = (
            aws_sdk_compute_optimizer.types.lambda_function_recommendations.deserialize_aws_json_1_0(
                data["lambdaFunctionRecommendations"]
            )
        )
    return out
