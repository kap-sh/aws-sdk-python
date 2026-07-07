"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeMetricAttributionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DescribeMetricAttributionRequest(TypedDict, closed=True):
    metric_attribution_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The metric attribution's Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetricAttributionRequest) -> dict:
    out: dict = {}
    out["metricAttributionArn"] = value["metric_attribution_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetricAttributionRequest:
    out: DescribeMetricAttributionRequest = {}  # type: ignore[typeddict-item]
    if "metricAttributionArn" in data:
        out["metric_attribution_arn"] = data["metricAttributionArn"]
    else:
        raise DeserializationError(
            "DescribeMetricAttributionRequest.metric_attribution_arn required"
        )
    return out
