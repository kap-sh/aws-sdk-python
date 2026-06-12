"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEC2InstanceRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_ids
    import aws_sdk_compute_optimizer.types.filters
    import aws_sdk_compute_optimizer.types.instance_arns
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.recommendation_preferences


class GetEC2InstanceRecommendationsRequest(TypedDict):
    instance_arns: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_arns.InstanceArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the instances for which to return recommendations.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of instance recommendations.</p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of instance recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["aws_sdk_compute_optimizer.types.filters.Filters"]
    """<p>An array of objects to specify a filter that returns a more specific list of instance recommendations.</p>"""
    account_ids: NotRequired["aws_sdk_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return instance recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return instance recommendations.</p> <p>Only one account ID can be specified per request.</p>"""
    recommendation_preferences: NotRequired[
        "aws_sdk_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]
    """<p>An object to specify the preferences for the Amazon EC2 instance recommendations to return in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEC2InstanceRecommendationsRequest) -> dict:
    out: dict = {}
    if "instance_arns" in value:
        import aws_sdk_compute_optimizer.types.instance_arns

        out["instanceArns"] = (
            aws_sdk_compute_optimizer.types.instance_arns.serialize_aws_json_1_0(
                value["instance_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.filters

        out["filters"] = aws_sdk_compute_optimizer.types.filters.serialize_aws_json_1_0(
            value["filters"]
        )
    if "account_ids" in value:
        import aws_sdk_compute_optimizer.types.account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "recommendation_preferences" in value:
        import aws_sdk_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEC2InstanceRecommendationsRequest:
    out: GetEC2InstanceRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "instanceArns" in data:
        import aws_sdk_compute_optimizer.types.instance_arns

        out["instance_arns"] = (
            aws_sdk_compute_optimizer.types.instance_arns.deserialize_aws_json_1_0(
                data["instanceArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    if "accountIds" in data:
        import aws_sdk_compute_optimizer.types.account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "recommendationPreferences" in data:
        import aws_sdk_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            aws_sdk_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out
