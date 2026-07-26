"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateMetricAttributionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class UpdateMetricAttributionResponse(TypedDict, closed=True):
    metric_attribution_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the metric attribution that you updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMetricAttributionResponse) -> dict:
    out: dict = {}
    if "metric_attribution_arn" in value:
        out["metricAttributionArn"] = value["metric_attribution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMetricAttributionResponse:
    out: UpdateMetricAttributionResponse = {}  # type: ignore[typeddict-item]
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    return out
