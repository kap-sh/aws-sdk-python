"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetAutoScalingGroupRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_ids
    import capo_compute_optimizer.types.auto_scaling_group_arns
    import capo_compute_optimizer.types.filters
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.recommendation_preferences


class GetAutoScalingGroupRecommendationsRequest(TypedDict, closed=True):
    account_ids: NotRequired["capo_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return Auto Scaling group recommendations.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return Auto Scaling group recommendations.</p> <p>Only one account ID can be specified per request.</p>"""
    auto_scaling_group_arns: NotRequired[
        "capo_compute_optimizer.types.auto_scaling_group_arns.AutoScalingGroupArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the Auto Scaling groups for which to return recommendations.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of Auto Scaling group recommendations.</p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of Auto Scaling group recommendations to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired["capo_compute_optimizer.types.filters.Filters"]
    """<p>An array of objects to specify a filter that returns a more specific list of Auto Scaling group recommendations.</p>"""
    recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.recommendation_preferences.RecommendationPreferences"
    ]
    """<p>An object to specify the preferences for the Auto Scaling group recommendations to return in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAutoScalingGroupRecommendationsRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import capo_compute_optimizer.types.account_ids

        out["accountIds"] = (
            capo_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "auto_scaling_group_arns" in value:
        import capo_compute_optimizer.types.auto_scaling_group_arns

        out["autoScalingGroupArns"] = (
            capo_compute_optimizer.types.auto_scaling_group_arns.serialize_aws_json_1_0(
                value["auto_scaling_group_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_compute_optimizer.types.filters

        out["filters"] = capo_compute_optimizer.types.filters.serialize_aws_json_1_0(
            value["filters"]
        )
    if "recommendation_preferences" in value:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendationPreferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.serialize_aws_json_1_0(
                value["recommendation_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAutoScalingGroupRecommendationsRequest:
    out: GetAutoScalingGroupRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_compute_optimizer.types.account_ids

        out["account_ids"] = (
            capo_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "autoScalingGroupArns" in data:
        import capo_compute_optimizer.types.auto_scaling_group_arns

        out["auto_scaling_group_arns"] = (
            capo_compute_optimizer.types.auto_scaling_group_arns.deserialize_aws_json_1_0(
                data["autoScalingGroupArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import capo_compute_optimizer.types.filters

        out["filters"] = capo_compute_optimizer.types.filters.deserialize_aws_json_1_0(
            data["filters"]
        )
    if "recommendationPreferences" in data:
        import capo_compute_optimizer.types.recommendation_preferences

        out["recommendation_preferences"] = (
            capo_compute_optimizer.types.recommendation_preferences.deserialize_aws_json_1_0(
                data["recommendationPreferences"]
            )
        )
    return out
