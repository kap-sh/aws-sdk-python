"""Generated from Smithy shape ``com.amazonaws.personalize#ListMetricAttributionMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.metric_attributes
    import aws_sdk_personalize.types.next_token


class ListMetricAttributionMetricsResponse(TypedDict):
    metrics: NotRequired["aws_sdk_personalize.types.metric_attributes.MetricAttributes"]
    """<p>The metrics for the specified metric attribution.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous <code>ListMetricAttributionMetricsResponse</code> request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMetricAttributionMetricsResponse) -> dict:
    out: dict = {}
    if "metrics" in value:
        import aws_sdk_personalize.types.metric_attributes

        out["metrics"] = (
            aws_sdk_personalize.types.metric_attributes.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMetricAttributionMetricsResponse:
    out: ListMetricAttributionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "metrics" in data:
        import aws_sdk_personalize.types.metric_attributes

        out["metrics"] = (
            aws_sdk_personalize.types.metric_attributes.deserialize_aws_json_1_1(
                data["metrics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
