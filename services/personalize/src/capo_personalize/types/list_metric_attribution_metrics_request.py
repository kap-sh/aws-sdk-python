"""Generated from Smithy shape ``com.amazonaws.personalize#ListMetricAttributionMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.max_results
    import capo_personalize.types.next_token


class ListMetricAttributionMetricsRequest(TypedDict, closed=True):
    metric_attribution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the metric attribution to retrieve attributes for.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of metrics to return in one page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMetricAttributionMetricsRequest) -> dict:
    out: dict = {}
    if "metric_attribution_arn" in value:
        out["metricAttributionArn"] = value["metric_attribution_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMetricAttributionMetricsRequest:
    out: ListMetricAttributionMetricsRequest = {}  # type: ignore[typeddict-item]
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
