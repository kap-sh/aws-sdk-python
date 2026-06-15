"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetLambdaFunctionRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_ids
    import aws_sdk_compute_optimizer.types.function_arns
    import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token


class GetLambdaFunctionRecommendationsRequest(TypedDict):
    function_arns: NotRequired[
        "aws_sdk_compute_optimizer.types.function_arns.FunctionArns"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the functions for which to return recommendations.</p> <p>You can specify a qualified or unqualified ARN. If you specify an unqualified ARN without a function version suffix, Compute Optimizer will return recommendations for the latest (<code>$LATEST</code>) version of the function. If you specify a qualified ARN with a version suffix, Compute Optimizer will return recommendations for the specified function version. For more information about using function versions, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html#versioning-versions-using\">Using versions</a> in the <i>Lambda Developer Guide</i>.</p>"""
    account_ids: NotRequired["aws_sdk_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return function recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return function recommendations.</p> <p>Only one account ID can be specified per request.</p>"""
    filters: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters.LambdaFunctionRecommendationFilters"
    ]
    """<p>An array of objects to specify a filter that returns a more specific list of function recommendations.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of function recommendations.</p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of function recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetLambdaFunctionRecommendationsRequest) -> dict:
    out: dict = {}
    if "function_arns" in value:
        import aws_sdk_compute_optimizer.types.function_arns

        out["functionArns"] = (
            aws_sdk_compute_optimizer.types.function_arns.serialize_aws_json_1_0(
                value["function_arns"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_compute_optimizer.types.account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetLambdaFunctionRecommendationsRequest:
    out: GetLambdaFunctionRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "functionArns" in data:
        import aws_sdk_compute_optimizer.types.function_arns

        out["function_arns"] = (
            aws_sdk_compute_optimizer.types.function_arns.deserialize_aws_json_1_0(
                data["functionArns"]
            )
        )
    if "accountIds" in data:
        import aws_sdk_compute_optimizer.types.account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.lambda_function_recommendation_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
