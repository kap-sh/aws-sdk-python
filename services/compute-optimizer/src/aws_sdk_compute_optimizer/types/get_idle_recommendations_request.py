"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetIdleRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_ids
    import aws_sdk_compute_optimizer.types.idle_max_results
    import aws_sdk_compute_optimizer.types.idle_recommendation_filters
    import aws_sdk_compute_optimizer.types.next_token
    import aws_sdk_compute_optimizer.types.order_by
    import aws_sdk_compute_optimizer.types.resource_arns


class GetIdleRecommendationsRequest(TypedDict, closed=True):
    resource_arns: NotRequired[
        "aws_sdk_compute_optimizer.types.resource_arns.ResourceArns"
    ]
    """<p>The ARN that identifies the idle resource.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of idle resource recommendations.</p>"""
    max_results: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_max_results.IdleMaxResults"
    ]
    """<p>The maximum number of idle resource recommendations to return with a single request. </p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""
    filters: NotRequired[
        "aws_sdk_compute_optimizer.types.idle_recommendation_filters.IdleRecommendationFilters"
    ]
    """<p>An array of objects to specify a filter that returns a more specific list of idle resource recommendations.</p>"""
    account_ids: NotRequired["aws_sdk_compute_optimizer.types.account_ids.AccountIds"]
    """<p>Return the idle resource recommendations to the specified Amazon Web Services account IDs.</p> <p>If your account is the management account or the delegated administrator of an organization, use this parameter to return the idle resource recommendations to specific member accounts.</p> <p>You can only specify one account ID per request.</p>"""
    order_by: NotRequired["aws_sdk_compute_optimizer.types.order_by.OrderBy"]
    """<p>The order to sort the idle resource recommendations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIdleRecommendationsRequest) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import aws_sdk_compute_optimizer.types.resource_arns

        out["resourceArns"] = (
            aws_sdk_compute_optimizer.types.resource_arns.serialize_aws_json_1_0(
                value["resource_arns"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_compute_optimizer.types.account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "order_by" in value:
        import aws_sdk_compute_optimizer.types.order_by

        out["orderBy"] = (
            aws_sdk_compute_optimizer.types.order_by.serialize_aws_json_1_0(
                value["order_by"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIdleRecommendationsRequest:
    out: GetIdleRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "resourceArns" in data:
        import aws_sdk_compute_optimizer.types.resource_arns

        out["resource_arns"] = (
            aws_sdk_compute_optimizer.types.resource_arns.deserialize_aws_json_1_0(
                data["resourceArns"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_compute_optimizer.types.idle_recommendation_filters

        out["filters"] = (
            aws_sdk_compute_optimizer.types.idle_recommendation_filters.deserialize_aws_json_1_0(
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
    if "orderBy" in data:
        import aws_sdk_compute_optimizer.types.order_by

        out["order_by"] = (
            aws_sdk_compute_optimizer.types.order_by.deserialize_aws_json_1_0(
                data["orderBy"]
            )
        )
    return out
