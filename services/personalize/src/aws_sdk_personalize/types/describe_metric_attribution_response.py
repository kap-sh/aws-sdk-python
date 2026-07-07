"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeMetricAttributionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.metric_attribution


class DescribeMetricAttributionResponse(TypedDict, closed=True):
    metric_attribution: NotRequired[
        "aws_sdk_personalize.types.metric_attribution.MetricAttribution"
    ]
    """<p>The details of the metric attribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetricAttributionResponse) -> dict:
    out: dict = {}
    if "metric_attribution" in value:
        import aws_sdk_personalize.types.metric_attribution

        out["metricAttribution"] = (
            aws_sdk_personalize.types.metric_attribution.serialize_aws_json_1_1(
                value["metric_attribution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetricAttributionResponse:
    out: DescribeMetricAttributionResponse = {}  # type: ignore[typeddict-item]
    if "metricAttribution" in data:
        import aws_sdk_personalize.types.metric_attribution

        out["metric_attribution"] = (
            aws_sdk_personalize.types.metric_attribution.deserialize_aws_json_1_1(
                data["metricAttribution"]
            )
        )
    return out
