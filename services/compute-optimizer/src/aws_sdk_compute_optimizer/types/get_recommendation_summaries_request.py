"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.account_ids
    import aws_sdk_compute_optimizer.types.max_results
    import aws_sdk_compute_optimizer.types.next_token


class GetRecommendationSummariesRequest(TypedDict, closed=True):
    account_ids: NotRequired["aws_sdk_compute_optimizer.types.account_ids.AccountIds"]
    """<p>The ID of the Amazon Web Services account for which to return recommendation summaries.</p> <p>If your account is the management account of an organization, use this parameter to specify the member account for which you want to return recommendation summaries.</p> <p>Only one account ID can be specified per request.</p>"""
    next_token: NotRequired["aws_sdk_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of recommendation summaries.</p>"""
    max_results: NotRequired["aws_sdk_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of recommendation summaries to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationSummariesRequest) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_compute_optimizer.types.account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer.types.account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationSummariesRequest:
    out: GetRecommendationSummariesRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_compute_optimizer.types.account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer.types.account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
