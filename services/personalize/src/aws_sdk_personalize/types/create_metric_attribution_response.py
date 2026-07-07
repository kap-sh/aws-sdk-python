"""Generated from Smithy shape ``com.amazonaws.personalize#CreateMetricAttributionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class CreateMetricAttributionResponse(TypedDict, closed=True):
    metric_attribution_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the new metric attribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMetricAttributionResponse) -> dict:
    out: dict = {}
    if "metric_attribution_arn" in value:
        out["metricAttributionArn"] = value["metric_attribution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMetricAttributionResponse:
    out: CreateMetricAttributionResponse = {}  # type: ignore[typeddict-item]
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    return out
