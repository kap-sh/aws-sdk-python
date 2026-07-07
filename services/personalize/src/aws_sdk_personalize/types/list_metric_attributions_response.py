"""Generated from Smithy shape ``com.amazonaws.personalize#ListMetricAttributionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.metric_attributions
    import aws_sdk_personalize.types.next_token


class ListMetricAttributionsResponse(TypedDict, closed=True):
    metric_attributions: NotRequired[
        "aws_sdk_personalize.types.metric_attributions.MetricAttributions"
    ]
    """<p>The list of metric attributions.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMetricAttributionsResponse) -> dict:
    out: dict = {}
    if "metric_attributions" in value:
        import aws_sdk_personalize.types.metric_attributions

        out["metricAttributions"] = (
            aws_sdk_personalize.types.metric_attributions.serialize_aws_json_1_1(
                value["metric_attributions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMetricAttributionsResponse:
    out: ListMetricAttributionsResponse = {}  # type: ignore[typeddict-item]
    if "metricAttributions" in data:
        import aws_sdk_personalize.types.metric_attributions

        out["metric_attributions"] = (
            aws_sdk_personalize.types.metric_attributions.deserialize_aws_json_1_1(
                data["metricAttributions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
